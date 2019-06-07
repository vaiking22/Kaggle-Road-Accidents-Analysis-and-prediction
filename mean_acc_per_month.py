import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

count = 0;
mean_month =[]
mean_month_acc =[]
for month in data_month.columns[2:-1]:
    for i in data_month.index :
        mean_month.append(data_month.loc[i,month])
    acc = (month,np.mean(mean_month))
    mean_month =[]
    mean_month_acc.append(acc)
    
mean_month_acc    
    
