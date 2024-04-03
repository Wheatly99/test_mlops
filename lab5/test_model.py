import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error


model = joblib.load("model.pkl")

def test_norm1_file():

    df = pd.read_excel('data/data2.xlsx')

    predict = model.predict(df[['x', 'y']])

    score = mean_absolute_error(predict, df.target)

    assert score < 0.3


def test_norm2_file():

    df = pd.read_excel('data/data3.xlsx')

    predict = model.predict(df[['x', 'y']])

    score = mean_absolute_error(predict, df.target)

    assert score < 0.3


def test_noise_file():

    df_noise = pd.read_excel('data/data_noise.xlsx')

    predict_noise = model.predict(df_noise[['x', 'y']])

    score_noise = mean_absolute_error(predict_noise, df_noise.target)

    assert score_noise < 0.3
