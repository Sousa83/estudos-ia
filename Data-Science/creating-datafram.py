#Biblioteca para manipulação de dataframes
import pandas as pd

dic = {
  'students': ['ricardo', 'aline', 'herran', 'patrick', 'grabiel'],
  'age': [19, 17, 18, 18, 18],
  'note': [8.9, 8.9, 7.9, 10.0, 9.99]
}

#Criando dataframe a partir da estrutura entitulada "dic"
df = pd.DataFrame(dic, columns=['students', 'age', 'note'])

#Coleção de informações gerais sobre o dataframe
df.describe()

#Dropa a primeira linha do dataframe
df.drop([0, 1])

#Exclui a coluna do df
df = df.drop('age', axis=1)

