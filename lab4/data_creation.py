from catboost.datasets import titanic
import pandas as pd

titanic_train, titanic_test = titanic()
df = pd.concat([titanic_train, titanic_test], ignore_index=True)
df.to_excel('data/data.xlsx', index=False)
