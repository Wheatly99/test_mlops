#!/usr/bin/python3
from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd

def create_model():

    df_train = pd.read_csv('train/train_data.csv', sep='~')

    model = LogisticRegression(random_state=42)
    model.fit(df_train.drop(columns={'target'}), df_train.target)
    joblib.dump(model, 'model.pkl')

if __name__ == '__main__':
    create_model()