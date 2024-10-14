#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#path
folder_path = os.path.join(os.getcwd(), "Training_Data")
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.csv') or f.endswith('.xls')]

all_data = []
#load data
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    #print(f"處理檔案: {excel_file}")
    
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    all_data.append(df)

feature = []
label = []

for df in all_data:   
    X = df[['LocationCode', 'WindSpeed(m/s)', 'Pressure(hpa)', 'Temperature(°C)', 'Humidity(%)', 'Sunlight(Lux)']]
    y = df['Power(mW)']
    
    feature.append(X)
    label.append(y)

print("read completed")

