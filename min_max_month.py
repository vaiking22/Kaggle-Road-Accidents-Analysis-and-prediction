import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder


data_month = pd.read_csv('only_road_accidents_data_month2.csv')
data_month.head()

# accidents per month
count = 0
month_acc =[]
for month in data_month.columns[2:-1]:
    for i in data_month.index:
        count = count + data_month.loc[i,month]
    acc = (month,count)
    month_acc.append(acc)
    count = 0




#months of max and min accidents

minvalue = month_acc[0]
maxvalue = month_acc[0]
for x in month_acc:
    if x[1] < minvalue[1]:
        minvalue =x
    if x[1] > maxvalue[1]:
        maxvalue =x
        
