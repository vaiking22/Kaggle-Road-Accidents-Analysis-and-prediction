import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

year_acc_mean=[]
year_acc =[]
data = pd.read_csv('road-accidents-in-india/only_road_accidents_data3.csv')

for year in data['YEAR'].unique():
    for i in data.index:
        if data.loc[i,'YEAR'] == year :
            year_acc.append(data.loc[i,'Total'])
    mean = np.mean(year_acc)
    year_mean =(year,mean)
    year_acc_mean.append(year_mean)
    mean =0
    year_acc =[]
year_acc_mean=set(list(year_acc_mean))
year_acc_mean
