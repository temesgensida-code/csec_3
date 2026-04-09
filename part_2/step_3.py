import pandas as ps

path="/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv"
reader = ps.read_csv(path)

#survival rate by gender
print(reader.groupby('Sex')['Survived'].mean())

#survival_rate_by_class 
print(reader.groupby('Pclass')['Survived'].mean())

#average age per class
print(reader.groupby('Pclass')['Age'].mean())

#survival rate by age group
reader['AgeGroup'] = ps.cut(reader['Age'], bins=[0, 18, 60, 100], labels=['Child', 'Adult', 'Senior'])
print(reader.groupby('AgeGroup')['Survived'].mean())
