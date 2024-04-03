import pandas as pd
import numpy as np

np.random.seed(0)

def create_noise_data():
    x = np.linspace(2, 8, 100)
    y = x + np.random.random(100) - 1
    y[25:45] *= 2
    z = x + y + np.random.random(100)

    df = pd.DataFrame({'x': x, 'y': y, 'target': z})
    df.to_excel('data/data_noise.xlsx', index=False)

if __name__ == '__main__':
  create_noise_data()