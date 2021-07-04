#!/usr/bin/env python3

## This code produces two datasets for the [Australian Public Service census](https://data.gov.au/data/dataset/2020-aps-employee-census):
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

## path to save
path = os.path.join("..","summer21","DANA4830","Proj")

### savefig
def savePNG(f):
    fName = f+".png"
    fPath = os.path.join(path,fName)
    plt.savefig(fPath, dpi=300)
    
### save df as csv
def saveCSV(f,fName):
    fName2 = fName+".csv"
    fPath = os.path.join(path,fName2)
    f.to_csv(fPath)

## load 2020 data
d20Cat = pd.read_csv(os.path.join(path,"2020-aps-employee-census-dataset.csv"))

## compute tick positions
tick = [d20Cat.keys()[0], d20Cat.keys()[1], d20Cat.keys()[2], d20Cat.keys()[3]]
tick_ix = [0, 1, 2, 3]

for j in range(4, d20Cat.shape[1]):
    if d20Cat.keys()[j-1][:3] != d20Cat.keys()[j][:3]:
        tick.append(d20Cat.keys()[j])
        tick_ix.append(j)
        
## plot
plt.figure(figsize=(16,12))
plt.subplot(2,1,1)
naPercentage = (d20Cat == " ").mean()
naPercentage = naPercentage[naPercentage > 0]
plt.bar(naPercentage.index, naPercentage.values)
plt.xticks(tick_ix, tick, rotation='vertical', size=10)
plt.ylabel("percentage of 'empty' in the columns")
plt.title("empty entries in raw data")

plt.subplot(2,1,2)
naPercentage2 = (d20Cat.T == " ").mean()
naPercentage2 = naPercentage2[naPercentage2 > 0]
plt.bar(naPercentage2.index, naPercentage2.values)
plt.ylabel("% of 'empty' in the rows")

plt.tight_layout()
savePNG("NAperColumn")

# 2020.1 EXTRACT SECTIONS THAT ARE COMPLETELY MISSING

## boolean is True for all empty cells
d20Emp = d20Cat == " "
d20PerColumn = {}

## check if all sub-question columns are empty per question
for tix in range(1,len(tick_ix)):
    cc = [d20Cat.keys()[ii] for ii in range(tick_ix[tix-1], tick_ix[tix])]
    d20PerColumn[tick[tix-1]] = np.all(d20Emp[cc], axis=1).mean()
d20PerColumn[tick[-1]] = np.all(d20Emp[d20Emp.keys()[tick_ix[tix]:]], axis=1).mean()
d20PerColumn = pd.Series(d20PerColumn)

## plot all missing percentage per question (group all subquestions per question)
plt.figure(figsize=(16,6))
plt.bar(d20PerColumn.index, d20PerColumn.values)
plt.xticks(rotation='vertical', size=12)
plt.ylabel("percentage of NA")
plt.title("Missing values per question (including all sub-sections)")

plt.tight_layout()
savePNG("NAperQuestion")

# 2020.2 CONVERT CATEGORICAL TO VALUES

def categorical_convert(x):
    X = x.copy()
    kk = list(x.keys())
    
    for j in kk:
        uni = x[j].unique()
        if ("Strongly agree" in uni):
            X[j][X[j] == "Strongly agree"]             = 1
            X[j][X[j] == "Agree"]                      = 2
            X[j][X[j] == "Neither agree nor disagree"] = 3
            X[j][X[j] == "Disagree"]                   = 4
            X[j][X[j] == "Strongly disagree"]          = 5
            X[j][X[j] == "Do not know"]                = 6
            X[j][X[j] == " "]                          = np.nan
            
        elif ("Tick" in uni):
            X[j][X[j] == "Tick"] = 1
            X[j][X[j] == " "]    = 0
            
        elif ("No" in uni):
            X[j][X[j] == "Yes"]                        = 1
            X[j][X[j] == "No"]                         = 2
            X[j][X[j] == "Not Sure"]                   = 3
            X[j][X[j] == "Not sure"]                   = 3
            X[j][X[j] == "Would prefer not to answer"] = 4
            X[j][X[j] == " "]                          = np.nan
            
        elif ("Impartial" in uni):
            X[j][X[j] == "Impartial"]            = 1
            X[j][X[j] == "Committed to service"] = 2
            X[j][X[j] == "Accountable"]          = 3
            X[j][X[j] == "Respectful"]           = 4
            X[j][X[j] == "Ethical"]              = 5
            X[j][X[j] == " "]                    = np.nan
            
        elif ("Positive change" in uni):
            X[j][X[j] == "Very positive change"] = 1
            X[j][X[j] == "Positive change"]      = 2
            X[j][X[j] == "No change"]            = 3
            X[j][X[j] == "Negative change"]      = 4
            X[j][X[j] == "Very negative change"] = 5
            X[j][X[j] == " "]                    = np.nan
            
        elif ("To a large extent" in uni):
            X[j][X[j] == "To a very large extent"] = 1
            X[j][X[j] == "To a large extent"]      = 2
            X[j][X[j] == "Somewhat"]               = 3
            X[j][X[j] == "To a small extent"]      = 4
            X[j][X[j] == "To a very small extent"] = 5
            X[j][X[j] == " "]                      = np.nan
            
        elif ("Don't know" in uni):
            X[j][X[j] == "Don't know"] = 0
            
        elif ("Male" in uni):
            X[j][X[j] == "Male"]                                   = 1
            X[j][X[j] == "Female"]                                 = 2
            X[j][X[j] == "X (Indeterminate/Intersex/Unspecified)"] = 3
            X[j][X[j] == "Prefer not to say"]                      = 4
            X[j][X[j] == " "]                                      = np.nan
            
        elif ("Under 40 years" in uni):
            X[j][X[j] == "Under 40 years"]    = 1
            X[j][X[j] == "40 to 54 years"]    = 2
            X[j][X[j] == "55 years or older"] = 3
            X[j][X[j] == " "]                 = np.nan
            
        elif ("To a great extent" in uni):
            X[j][X[j] == "Not at all"]             = 1
            X[j][X[j] == "Very little"]            = 2
            X[j][X[j] == "Somewhat"]               = 3
            X[j][X[j] == "To a great extent"]      = 4
            X[j][X[j] == "To a very great extent"] = 5
            X[j][X[j] == " "]                      = np.nan
            
        elif ("Often" in uni):
            X[j][X[j] == "Always"]    = 1
            X[j][X[j] == "Often"]     = 2
            X[j][X[j] == "Sometimes"] = 3
            X[j][X[j] == "Rarely"]    = 4
            X[j][X[j] == "Never"]     = 5
            X[j][X[j] == " "]         = np.nan
            
    return X

d20 = categorical_convert(d20Cat)

