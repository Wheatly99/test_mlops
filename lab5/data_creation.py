import pandas as pd
import numpy as np
import os

np.random.seed(0)

def create_new_data():

    os.mkdir('data')

    x1 = np.linspace(2, 8, 100)
    y1 = x1 + np.random.random(100) - 1
    z1 = x1 + y1 + np.random.random(100)

    df1 = pd.DataFrame({'x': x1, 'y': y1, 'target': z1})
    df1.to_excel('data/data1.xlsx', index=False)


    x2 = np.linspace(2, 8, 100)
    y2 = x2 + np.random.random(100) - 2
    z2 = x2 + y2 + np.random.random(100)

    df2 = pd.DataFrame({'x': x2, 'y': y2, 'target': z2})
    df2.to_excel('data/data2.xlsx', index=False)


    x3 = np.linspace(2, 8, 100)
    y3 = x3 + np.random.random(100) - 3
    z3 = x3 + y3 + np.random.random(100)

    df3 = pd.DataFrame({'x': x3, 'y': y3, 'target': z3})
    df3.to_excel('data/data3.xlsx', index=False)

if __name__ == '__main__':
  create_new_data()