import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
import numpy as np
from sklearn.linear_model import LinearRegression


state_acc = []
data = pd.read_csv('road-accidents-in-india/only_road_accidents_data3.csv')
state_acc_mean =[]
for state in data['STATE/UT'].unique():
    for i in data.index:
        if data.loc[i,'STATE/UT'] == state :
            state_acc.append(data.loc[i,'Total'])
    mean = np.mean(state_acc)
    state_mean =(state,mean)
    state_acc_mean.append(state_mean)
    mean =0
    state_acc =[]
state_acc_mean=set(list(state_acc_mean))
state_acc_mean
