import pandas as ps

path="/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv"
reader = ps.read_csv(path)
reader['Age'] = reader['Age'].fillna(reader['Age'].median())

reader['Embarked'] = reader['Embarked'].fillna(reader['Embarked'].mode()[0])

reader = reader.drop(columns=['Cabin'])

print(reader.info())
