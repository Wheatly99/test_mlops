import pandas as pd

df = pd.read_excel('data/data.xlsx')
df.Age = df.Age.fillna(df.Age.mean())
df.to_excel('data/data.xlsx', index=False)
