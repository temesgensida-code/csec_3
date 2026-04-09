import pandas as ps

path="/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv"
reader = ps.read_csv(path)
print(reader.head(1))
print(reader.info())
print(reader.describe())
