import pandas as pd

df = pd.read_excel('data/data.xlsx')
df_3_columns = df[['Pclass', 'Sex', 'Age']].copy()
df_3_columns.to_excel('data/data.xlsx', index=False)
