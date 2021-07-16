#!/usr/bin/env python3

## This code produces two datasets for the [Australian Public Service census](https://data.gov.au/data/dataset/aps_employee_census_2014/resource/9b44e035-3bed-40dc-9687-34fc47b9f228):
##
## 1. Extract ordinal variables for imputation
## 
## 2. Extract nominal varaibles, remove sections that are completely missing.
##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os

## fig configurations
plt.rcParams["figure.figsize"] = [10,4]
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=13)
plt.rcParams.update({'legend.fontsize': 11})
plt.rcParams.update({'axes.labelsize': 15})
plt.rcParams.update({'font.size': 15})

### savefig
def savePNG(f):
    fName = f+".png"
    fPath = os.path.join("figures",fName)
    plt.savefig(fPath, dpi=300)
    
### save df as csv
def saveCSV(f,fName):
    fName2 = fName+".csv"
    fPath = os.path.join("data",fName2)
    f.to_csv(fPath)

## load 2020 data
d14Cat = pd.read_csv(os.path.join("data","2014-aps-employee-census-5-point-dataset.csv"))

## compute tick positions
tick = [d14Cat.keys()[0], d14Cat.keys()[1], d14Cat.keys()[2], d14Cat.keys()[3]]
tick_ix = [0, 1, 2, 3]

for j in range(4, d14Cat.shape[1]):
    if d14Cat.keys()[j-1][:3] != d14Cat.keys()[j][:3]:
        tick.append(d14Cat.keys()[j])
        tick_ix.append(j)
        
## plot
plt.figure(figsize=(16,12))
plt.subplot(2,1,1)
naPercentage = (d14Cat == " ").mean()
naPercentage = naPercentage[naPercentage > 0]
plt.bar(naPercentage.index, naPercentage.values)
plt.xticks(tick_ix, tick, rotation='vertical', size=10)
plt.ylabel("percentage of 'empty' in the columns")
plt.title("empty entries in raw data")

plt.subplot(2,1,2)
naPercentage2 = (d14Cat.T == " ").mean()
naPercentage2 = naPercentage2[naPercentage2 > 0]
plt.bar(naPercentage2.index, naPercentage2.values)
plt.ylabel("% of 'empty' in the rows")

plt.tight_layout()
savePNG("NAperColumn")

# 2020.1 EXTRACT SECTIONS THAT ARE COMPLETELY MISSING

## boolean is True for all empty cells
d14Emp = d14Cat == " "
d14PerColumn = {}

## check if all sub-question columns are empty per question
for tix in range(1,len(tick_ix)):
    cc = [d14Cat.keys()[ii] for ii in range(tick_ix[tix-1], tick_ix[tix])]
    d14PerColumn[tick[tix-1]] = np.all(d14Emp[cc], axis=1).mean()
d14PerColumn[tick[-1]] = np.all(d14Emp[d14Emp.keys()[tick_ix[tix]:]], axis=1).mean()
d14PerColumn = pd.Series(d14PerColumn)

## plot all missing percentage per question (group all subquestions per question)
plt.figure(figsize=(16,6))
plt.bar(d14PerColumn.index, d14PerColumn.values)
plt.xticks(rotation='vertical', size=12)
plt.ylabel("percentage of NA")
plt.title("Missing values per question (including all sub-sections)")

plt.tight_layout()
savePNG("NAperQuestion")

## drop cols (selected manually by inspection)
drop_cols_init = ["q24.1", "q26.1", "q27", "q33.1", "q35", "q36", "q37", "q38", "q39.1", "q40.1",
                  "q41.1", "q44.1", "q45.1", "q55", "q56", "q57", "q59", "q60.1", "q62.1", "q64.1"
                  ]
def rm_cols(x, drp):
    drop_cols = []
    ix = dict(zip(tick, tick_ix))
    for k in range(len(drp)-1):
        i0 = ix[drp[k]]
        i1 = tick_ix[tick_ix.index(i0)+1]
        drop_cols += list(x[list(x.keys()[i0:i1].values)].keys())
    drop_cols += ["q64."+str(i) for i in range(1,14)]
    return drop_cols

# 2020.3 CONVERT CATEGORICAL TO VALUES

from categorical_convert import cat_convert

d14 = cat_convert(d14Cat)
drop_cols = rm_cols(d14, drop_cols_init)
d14Numerical = d14.drop(drop_cols, axis=1)
d14Nominal   = d14[drop_cols]


# 2020.4 IMPUTE DATASETS

from sklearn.linear_model import LinearRegression
from sklearn.impute import KNNImputer

## impute Numerical dataset
KNNImp = KNNImputer(n_neighbors=2)
KNNNum = KNNImp.fit_transform(np.array(d14Numerical))

## remove columns with too many missing values in Nominal dataset
del_cols = d14Nominal.keys()[d14Nominal.isna().mean() >= 0.4]
d14NomDrop = d14Nominal.drop(del_cols, axis=1)

## impute Nominal  dataset
KNNNom = KNNImp.fit_transform(np.array(d14NomDrop))

## combine into master dataframe
NumImp = pd.DataFrame(KNNNum, columns=d14Numerical.columns)
NomImp = pd.DataFrame(KNNNom, columns=d14NomDrop.columns)

cc = [ci for ci in d14Cat.keys() if ci not in del_cols]

d14Master_aux = pd.concat([NumImp, NomImp], axis=1)
d14Master = np.round(d14Master_aux[cc])

## save Master dataset
saveCSV(d14Master, "d14Master")

