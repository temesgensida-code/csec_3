# PART1 : defining a dataframe from a pure python dictionary
on this first part i have tried to define a panadas dataframe from python dictionary
# PART2: Titanic Dataset Analysis

This directory contains an exploratory data analysis of the Titanic dataset. The goal of this exercise is to understand passenger demographics and determine the key factors that influenced survival rates during the disaster (such as gender, passenger class, and age).

## How Each Step Was Solved

The solution is broken down into a series of Python scripts, culminating in a summary of the insights:

* **Step 1: Loading and Exploring Data (`step_1.py`)**  
  Loaded the Kaggle Titanic CSV using `pandas` and displayed the initial structure of the data using `.head()`, `.info()`, and `.describe()` to understand distributions and identify missing values.

* **Step 2: Data Cleaning (`step_2.py`)**  
  Handled missing data to prepare for analysis: 
  - Filled missing `Age` values with the median age.
  - Filled missing `Embarked` categories with the mode (most frequent port).
  - Dropped the `Cabin` column entirely due to too many missing values.

* **Step 3: Aggregation and Grouping (`step_3.py`)**  
  Used `.groupby()` to calculate average survival rates across different demographics. Sliced the data to find survival rates by gender and passenger class. Also, bucketed continuous `Age` data into categories ('Child', 'Adult', 'Senior') using `pd.cut()` to analyze survival rates by age group.

* **Step 4: Data Filtering (`step_4.py`)**  
  Applied boolean masking (filtering) to isolate specific high-priority groups that survived:
  - Extracted all female passengers who survived.
  - Extracted all children (age under 18) who survived.

* **Step 5: Insights and Conclusions (`step_5.txt`)**  
  Gathered the empirical data from the previous steps to formally answer questions about survival probability, notably confirming the "women and children first" maritime tradition and the strong impact of socio-economic class.

## Kaggle Notebook Reference

You can review the full Kaggle notebook for this project here:  
**URL FOR KAGGLE:** [https://www.kaggle.com/code/temesgensida/notebookcb5d0ca70d](https://www.kaggle.com/code/temesgensida/notebookcb5d0ca70d)
