from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from pathlib import Path


def creating_data():

    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
    X_train, X_test, y_train, y_test = train_test_split(df.drop(columns={'target'}), df.target,
                                                        random_state=42, stratify=df.target)
    X_train['target'] = y_train
    X_test['target'] = y_test

    Path("train").mkdir(parents=True, exist_ok=True)
    Path("test").mkdir(parents=True, exist_ok=True)

    print(y_testasdasd)

    X_train.to_csv('train/train_data.csv', index=False, sep='~')
    X_test.to_csv('test/test_data.csv', index=False, sep='~')


if __name__ == '__main__':
    creating_data()