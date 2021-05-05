import pandas as pd

dic = {
  'students': ['ricardo', 'aline', 'herran', 'patrick', 'grabiel'],
  'age': [19, 17, 18, 18, 18],
  'note': [8.9, 8.9, 7.9, 10.0, 9.99]
}

df = pd.DataFrame(dic, columns=['students', 'age', 'note'])

#Os comandos a seguir, fazem as operações, em uma determinada coluna, em todas as linhas
df['note'].add(10)

df['note'].sub(10)

df['note'].mul(10)

df['note'].div(10)
