#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import matplotlib.pyplot as plt
from tqdm import tqdm 

stations = 17
for n in range(stations):
    if(n + 1 < 10):
        station_num = '0' + str(n + 1)
    else:
        station_num = str(n + 1)
    data_directory = os.getcwd() + "/LSTM+迴歸分析(比賽用)/ExampleTrainData(AVG)"
    data_file = os.path.join(data_directory, 'AvgDATA_' + station_num + '.csv')  
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"not found：{data_file}")

    data = pd.read_csv(data_file)

    if 'Serial' in data.columns:
        data = data.drop('Serial', axis=1)
        print("'Serial' error")

    X = data.drop('Power(mW)', axis=1)
    y = data['Power(mW)']


    numerical_features = ['WindSpeed(m/s)', 'Pressure(hpa)', 
                        'Temperature(°C)', 'Humidity(%)', 'Sunlight(Lux)']

    for feature in numerical_features:
        if feature not in X.columns:
            raise ValueError(f"特徵 '{feature}' 不存在於資料中")

    preprocessor = StandardScaler()

    pipeline = Pipeline(steps=[
        ('scaler', preprocessor),
        ('regressor', LinearRegression())
    ])

    train_size = 0.8 
    num_experiments = 100     

    Ein_list = []
    Eout_list = []
    MAE_list = []
    all_predictions = []


    rng = np.random.default_rng(seed=42)

    for i in tqdm(range(num_experiments), desc="iter"):
        random_state = rng.integers(0, 100000)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, train_size=train_size, test_size=1 - train_size, random_state=random_state)

        pipeline.fit(X_train, y_train)

        y_train_pred = pipeline.predict(X_train)
        y_test_pred = pipeline.predict(X_test)

        Ein = mean_squared_error(y_train, y_train_pred)
        Eout = mean_squared_error(y_test, y_test_pred)
        MAE = mean_absolute_error(y_test, y_test_pred)

        Ein_list.append(Ein)
        Eout_list.append(Eout)
        MAE_list.append(MAE)

        predictions_df = pd.DataFrame({
            'Experiment': i+1,
            'Actual': y_test.values,
            'Predicted': y_test_pred
        })
        all_predictions.append(predictions_df)

    # print(all_predictions)

    # print("end")
    all_predictions_df = pd.concat(all_predictions, ignore_index=True)
    # print(all_predictions_df)
    average_MAE = np.mean(MAE_list)
    std_MAE = np.std(MAE_list)
    print(f"Station {station_num}:")
    print(f"average: {average_MAE:.4f}")
    print(f"sigma: {std_MAE:.4f}")