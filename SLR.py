import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
import numpy as np
from sklearn.linear_model import LinearRegression




model = LinearRegression()
X_data = np.array([t[0] for t in e])
Y_data = np.array([y[1] for y in e])
model.fit(X_data.reshape(len(X_data),1),Y_data.reshape(len(Y_data),1))
plt.scatter(X_data,Y_data,color='black')
#plt.plot(model.predict(x.reshape(len(x),1)))
plt.plot(X_data,model.predict(X_data.reshape(len(X_data),1)),color='blue') # to plot the line of regression

