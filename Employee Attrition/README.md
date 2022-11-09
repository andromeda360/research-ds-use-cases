## EMPLOYEE ATTRITION PREDICTION USING MACHINE LEARNING

### Problem:
Attrition in human resources refers to the gradual loss of employees over time. In general, relatively high attrition is problematic for companies. HR professionals often assume a leadership role in designing company compensation programs, work culture and motivation systems that help the organization retain top employees.

### Goal:
Our goal is to uncover the factors that lead to employee attrition through Exploratory Data Analysis and explore them by using various classification models to predict if an employee is likely to quit. This could greatly increase HR’s ability to intervene on time and remedy the situation to prevent attrition.

### Data:
The dataset we use is publicly available and can be accessed from [here](https://excelbianalytics.com/wp/downloads-21-sample-csv-files-data-sets-for-testing-till-5-million-records-hr-analytics-for-attrition/).

The dataset has (1000000R X 35C) that contains numeric and categorical data types describing each employee’s background and characteristics; and labelled (supervised learning) with whether they are still in the company or whether they have gone to work somewhere else. Machine Learning models can help to understand and determine how these factors relate to workforce attrition.

### Problem Type:
Classification

### 1)Employee Attrition EDA:
*	checking for the null values.
*	checking for the duplicate values.
*	Univariate Analysis
*	Bivariate Analysis
*	Multivariate Analysis

### 2)Employee Attrition Preprocessing:
* Checking for outliers
* Data Cleaning
* Pearson Correlation
* One-Hot Encoding
* Feature Scaling(Normalization)

### 3)Employee Attrition feature selection:

##### Initial model building using evalML without feature selection
#### Feature Selection
##### Feature importance using random forest classifier (Selected top 21 features):
comment: After selecting important features we applied some algorithms and most of them attain 50% accuracy.
##### Feature selection using SelectKBest (Selected top 15 features):
comment: Important features were selected using SelectKBest and we applied some algorithms and most of them attain 50% accuracy.

### 4)Employee Attrition Model-1:

comment: After performing feature selection most of the models encountered with the lower accuracy of 50% , so we decided to keep all the features for model building.
#### Model Building
We have trained and tested various machine learning classification models.

(https://github.com/Raeena-Firdous/Employee-Attrition/blob/main/4/Employee%20Attrition%20Model-1.ipynb)

### 5)Employee Attrition Model-2:

As we were getting lower accuracy from the model-1, so we have developed this model-2 by creating a new column "attrition_within_a_year" using "YearsAtCompany" column,
to see whether an employee get attritioned with in a year or not. We made this "attrition_within_a_year" feature as our dependent variable and dropped the "attrition" column from our dataset. 
Initially it was in imbalanced form, so for handling that we used a oversampling technique(SMOTE).
#### Model Building
We have trained and tested various machine learning classification models.

(https://github.com/Raeena-Firdous/Employee-Attrition/blob/main/5)Employee%20Attrition%20Model-2.ipynb)

