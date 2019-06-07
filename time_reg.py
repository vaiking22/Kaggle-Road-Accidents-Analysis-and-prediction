import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder


data = pd.read_csv('Prepared data v1.csv')
data =data.drop('Unnamed: 0',axis=1)
le1 = LabelEncoder()
le2 = LabelEncoder()

for i in data.index:
    if data.loc[i,'TIME']== '0-3 hrs. (Night)':
        data.loc[i,'TIME'] = 0
    elif data.loc[i,'TIME']== '3-6 hrs. (Night)':
        data.loc[i,'TIME'] = 1
    elif data.loc[i,'TIME']== '6-9 hrs (Day)':
        data.loc[i,'TIME'] = 2
    elif data.loc[i,'TIME']== '9-12 hrs (Day)':
        data.loc[i,'TIME'] = 3
    elif data.loc[i,'TIME']== '12-15 hrs (Day)':
        data.loc[i,'TIME'] = 4
    elif data.loc[i,'TIME']== '15-18 hrs (Day)':
        data.loc[i,'TIME'] = 5
    elif data.loc[i,'TIME']== '18-21 hrs (Night)':
        data.loc[i,'TIME'] = 6
    elif data.loc[i,'TIME']== '21-24 hrs (Night)':
        data.loc[i,'TIME'] = 7

data['STATE/UT']=le1.fit_transform(data['STATE/UT'])
#data['TIME'] = le2.fit_transform(data['TIME'])
data.loc[500]

ohe = OneHotEncoder(categorical_features=[0])
data_matrix_x= data[['STATE/UT','YEAR','TIME']].values
data_matrix_y = data.ACCIDENTS
data_matrix_x

ohe.fit(data_matrix_x)

data_matrix = ohe.transform(data_matrix_x).toarray()



data_matrix
data_matrix_y

model = LinearRegression(fit_intercept=False)
X_train ,X_test ,y_train, y_test = train_test_split(data_matrix,data_matrix_y ,test_size = 0.2)
model.fit(X_train,y_train)  
model.score(X_test,y_test)


cal = ohe.transform([[4,2016,4]])
cal = cal.toarray()
model.predict(cal)

