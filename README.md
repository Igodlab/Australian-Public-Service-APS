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

This should take some minutes. Then you can check in the data folder that they have been saved sepparately as `d20Nominal.csv` & `d20Numerical.csv`. Imputation for missing data is performed in the latter. After missing values have been dealt with, we convert all values into numbers (reffer to the explanatory table for more detailed reference) and finally merge the files back into a `d20Master.csv` **in progress**


