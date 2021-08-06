# An study of Leadership proxies in the Australian Public Service (APS)
This is an study of leadership in the APS based on the [2020 Census](https://data.gov.au/data/dataset/2020-aps-employee-census). The goal of this research is to find the collection of features that have greater weight in predicting traits of leadership among individuals.

## 1. The dataset
The data of the census corresponds to the [2020 Questionnaire](https://data.gov.au/data/dataset/2020-aps-employee-census/resource/d102ffb5-16be-4f99-a315-2a60c3f2f70f). It is a collection of 64 questions among which many contain multiple sub-questions, some of them are of a Binary answer-type, others are Nominal and Ordinal.

To get started, create a new directory named `data`, then download the [2020 dataset](https://data.gov.au/data/dataset/2020-aps-employee-census/resource/ed2f2993-99b4-4bf7-bc58-42bcd0136752) and save it there.

## 1.1 Data cleaning
There is a mix between true missing values and questions deliberately not answered. So an extensive analysis before discrimation of missingness is performed.

The first step is to take a look at the questionaire and select the columns that correspond to Nominal features (labeled as `drop_cols` in the code). Then, contrast those Nominal columns with the percentage of missing values in figure "NAperColumn.png" (located in `figures`). From these two observations decide which columns can be removed and which columns should remain for splitting the data into Nominal and numerical features.

To get all the figures and splitted datasets, just run the `dana30-masterDataset.py` in shell

```shell
$ ./dana30-masterDataset.py
```

This should take several minutes (~30-45 minutes). Then you can check in the data folder that they have been saved sepparately as `d20Nominal.csv` & `d20Numerical.csv`. Imputation for missing data is performed in the latter. After missing values have been dealt with, we convert all values into numbers (reffer to the explanatory table for more detailed reference) and finally merge the files back into a `d20Master.csv` 

Repeat the process for the 2014 dataset but using `dana30-2014masterDataset.py`, and you should get the cleaned `d14Master.csv`. 

## 2. Descriptive analysis

The code to run descriptive analysis can be found in 

## 3. Permuting and Bootstrapping methods for independence (`dana30-project.ipynb`)

Based on the ideas discussed in [Melissande A., Yann B. & Magalie F.](https://hal.archives-ouvertes.fr/hal-01001984v4/document) we have used computational methods for building up statistics by bootstrapping and permuting the samples of 2014 & 2020 and then compare their distributions to gain insight on iid. (independent identically distributed). The code that runs this tests is the last part of the notebook `dana30-project.ipynb`

## 4. Exploratory Factor Analysis (``)

 To extract the patterns embedded in Likert scale questions we perform an Exploratoriy Factor Analysis (EFA). The goal of EFA is to reduce the dimensionality of the feature space by re-scaling and rotating the axis of the coordinate system in which the features lie. 

 Therefore, it allows to find a reduced coordinate system called **Factors** $\bf F$, which are unobserved variables that capture the largest amount of variability among some features. The magnitude of how much a Factor can describe the initial features is determined by the **Loadings** $\bf L$, which define a linear combination of loads onto latent factors. The code that computes this is ``

 ## 5. Clustering and Classification (`dana30-project.ipynb`)


Confirm the findings of EFA with a visual representation of the Factors and features that lead to identify leadership styles. Use k-means algorothm to fund clusters. The code can be found in the middle part of the `dana30-project.ipynb` notebook.


