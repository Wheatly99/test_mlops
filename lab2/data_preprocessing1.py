#!/usr/bin/python3
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocessing():

    df_train = pd.read_csv('train/train_data.csv', sep='~')
    df_test = pd.read_csv('test/test_data.csv', sep='~')

    sc = StandardScaler()

    df_train[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']] = sc.fit_transform(
        df_train.drop(columns={'target'}))
    df_test[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']] = sc.transform(
        df_test.drop(columns={'target'}))

    df_train.to_csv('train/train_data.csv', index=False, sep='~')
    df_test.to_csv('test/test_data.csv', index=False, sep='~')

if __name__ == '__main__':
    preprocessing()
