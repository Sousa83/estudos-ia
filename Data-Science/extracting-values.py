import pandas as pd

dic = {
  'students': ['ricardo', 'aline', 'herran', 'patrick', 'grabiel'],
  'age': [19, 17, 18, 18, 18],
  'note': [8.9, 8.9, 7.9, 10.0, 9.99]
}

df = pd.DataFrame(dic, columns=['students', 'age', 'note'])

#Mostra a quantidade de linhas em cada coluna
df.count()

#Mostra as colunas do df
df.columns

#Mostra as linhas e colunas, respectivamente
df.shape
