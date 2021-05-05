import pandas as pd

dic = {
  'students': ['ricardo', 'aline', 'herran', 'patrick', 'grabiel'],
  'age': [19, 17, 18, 18, 18],
  'note': [8.9, 8.9, 7.9, 10.0, 9.99]
}

df = pd.DataFrame(dic, columns=['students', 'age', 'note'])

#Maior valor: em Strings são mostrados por ordem alfabetica
#As informações são sobre os dados sem relação alguma de registro
df.max()

df['age'].max()

#Menor valor
df.min()

#Média: String não é possível fazer médias
df.mean()

#Mediana
df.median()

#Soma: A soma, nas strings, é a concatenação
df.sum()
