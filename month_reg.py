import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder


#performing vectorization
i=0

new_data_month = pd.DataFrame(columns = ['STATE/UT','YEAR','MONTH','ACCIDENTS'],index = np.arange(10000))
for states in data_month['STATE/UT'].unique():
    for year in data_month['YEAR'].unique():
        for month in data_month.columns[2:-1]:
            new_data_month.loc[i,'STATE/UT']= states
            new_data_month.loc[i,'YEAR']= year
            new_data_month.loc[i,'MONTH']= month
            i=i+1   



j=0
for i in data_month.index:
    for month in data_month.columns[2:-1]:
        new_data_month.loc[j,'ACCIDENTS'] = data_month.loc[i,month]
        j=j+1
new_data_month=new_data_month.dropna(how = 'any',axis=0)


# Linear multiple regression

le_month_1 = LabelEncoder()
le_month_2 = LabelEncoder()
new_data_month['STATE/UT']=le_month_1.fit_transform(new_data_month['STATE/UT'])
new_data_month['MONTH']=le_month_2.fit_transform(new_data_month['MONTH'])


ohe = OneHotEncoder(categorical_features=[0,2])
data_month_matrix_x= new_data_month[['STATE/UT','YEAR','MONTH']].values
data_month_matrix_y = new_data_month.ACCIDENTS


ohe.fit(data_month_matrix_x)
data_matrix_month = ohe.transform(data_month_matrix_x).toarray()
model3 = LinearRegression(fit_intercept=False)
X_train ,X_test ,y_train, y_test = train_test_split(data_matrix_month,data_month_matrix_y ,test_size = 0.2)
model3.fit(X_train,y_train)
model3.score(X_test,y_test)



#to take input from user , this is an example input scenario
state = input('Give name of state')
year = int(input('Give year'))
month = input('Give month')

state = le_month_1.transform([state])
month = le_month_2.transform([month])

cal = ohe.transform([[state,year,month]])
model.predict(cal)
