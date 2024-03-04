import pandas as pd

df = pd.read_excel('data/data.xlsx')
y = pd.get_dummies(df.Sex, prefix='sex')
df_new = pd.merge(df, y, left_index=True, right_index=True).drop(columns={'Sex'})
df_new.to_excel('data/data.xlsx', index=False)
