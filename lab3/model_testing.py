import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def predict():

    df_test = pd.read_csv('test/test_data.csv', sep='~')

    model = joblib.load('model.pkl')

    pred = model.predict(df_test.drop(columns={'target'}))

    print(f'Accuracy - {accuracy_score(pred, df_test.target)}')

if __name__ == '__main__':
    predict()