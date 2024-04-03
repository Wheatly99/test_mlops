import joblib
import pandas as pd
from sklearn.metrics import accuracy_score


def test_upload_file():

    model = joblib.load("model.pkl")

    df1 = pd.read_excel('data/data2.xlsx')
    df2 = pd.read_excel('data/data3.xlsx')
    df_noise = pd.read_excel('data/data_noise.xlsx')

    predict1 = model.predict(df1[['x', 'y']])
    predict2 = model.predict(df2[['x', 'y']])
    predict_noise = model.predict(df_noise[['x', 'y']])

    score1 = accuracy_score(predict1, df1.z)
    score2 = accuracy_score(predict2, df2.z)
    score_noise = accuracy_score(predict_noise, df_noise.z)

    assert score1 > 80
    assert score2 > 80
    assert score_noise > 80
