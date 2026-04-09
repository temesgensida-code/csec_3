import pandas as ps

path="/kaggle/input/datasets/yasserh/titanic-dataset/Titanic-Dataset.csv"
reader = ps.read_csv(path)

#female passanger who has survived
females_survived = reader[(reader['Sex'] == 'female') & (reader['Survived'] == 1)]
print(females_survived.info())

#childern who has survived
children_survived = reader[(reader['Age'] < 18) & (reader['Survived'] == 1)]
print(children_survived.info())
