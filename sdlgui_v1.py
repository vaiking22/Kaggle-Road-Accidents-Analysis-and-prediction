import tkinter as tk
from tkinter import ttk
r=tk.Tk();
r.geometry("1000x1000+30+30")
r.title('Road Accident Analysis using Machile Learning')

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder


data = pd.read_csv('only_road_accidents_data3.csv')

data.head()

new_data=pd.read_csv('time_Prepared data v1.csv')


data = pd.read_csv('only_road_accidents_data3.csv')
e= []
cnt2 = 0
for year in data['YEAR'].unique():
    for i in data.index:
        if data.loc[i,'YEAR'] == year:
            cnt2 = cnt2 + data.loc[i,'Total'] 
    year_acc = (year,cnt2)
    cnt2=0
    e.append(year_acc)
         
model = LinearRegression()
X_data = np.array([t[0] for t in e])
Y_data = np.array([y[1] for y in e])
model.fit(X_data.reshape(len(X_data),1),Y_data.reshape(len(Y_data),1))

data = pd.read_csv('time_Prepared data v1.csv')
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
       
        
ohe.fit(data_matrix_x)
        
data_matrix = ohe.transform(data_matrix_x).toarray()
    
model1 = LinearRegression(fit_intercept=False)
X_train ,X_test ,y_train, y_test = train_test_split(data_matrix,data_matrix_y ,test_size = 0.2)
model1.fit(X_train,y_train)

new_data_month = pd.read_csv('prepared data month.csv')
le_month_1 = LabelEncoder()
le_month_2 = LabelEncoder()
new_data_month['STATE/UT']=le_month_1.fit_transform(new_data_month['STATE/UT'])
new_data_month['MONTH']=le_month_2.fit_transform(new_data_month['MONTH'])


ohe_month = OneHotEncoder(categorical_features=[0,2])
data_month_matrix_x= new_data_month[['STATE/UT','YEAR','MONTH']].values
data_month_matrix_y = new_data_month.ACCIDENTS


ohe_month.fit(data_month_matrix_x)
data_matrix_month = ohe_month.transform(data_month_matrix_x).toarray()
model3 = LinearRegression(fit_intercept=False)
X_train ,X_test ,y_train, y_test = train_test_split(data_matrix_month,data_month_matrix_y ,test_size = 0.2)
model3.fit(X_train,y_train)

def analysis():
    top1=tk.Toplevel(r)
    top1.geometry('500x500+30+30')
    top1.title('Analysis')
    
    #to find the timespan of max and min accidents
    c= []
    cnt = 0
    for time in data.columns[2:10]:
        for i in data.index:
            cnt  = cnt + data.loc[i,time]
        time_acc = (time,cnt)
        cnt=0
        c.append(time_acc)
    #print(c) 
    x = c[0]
    y = c[0]
    for i in c:
        if i[1]>x[1]:
            x = i
        if i[1] <y[1]:
            y=i
    msg1="Timespan of maximum accidents:"
    msg2="Timespan of minimum accidents:"

    def ab_prints(msg,a):
        #tk.messagebox.showinfo(msg,a)
        
        txt=tk.Toplevel(top1)
        txt.geometry("500x100+10+10")
        tt1=tk.Message(txt,text=msg,relief=tk.RAISED,anchor=tk.W,width=300)
        tt1.pack(padx=10,pady=5)
        tt2=tk.Message(txt,text=a,relief=tk.RAISED,anchor=tk.W,width=200)
        tt2.pack(padx=10,pady=5)
        #text=tk.Text(txt)
        #text.insert(tk.END,msg)
        #text.insert(tk.END,a)
        #text.pack()    

    def ab3():
        data_month = pd.read_csv('only_road_accidents_data_month2.csv')
        count = 0;
        mean_month =[]
        mean_month_acc =[]
        for month in data_month.columns[2:-1]:
            for i in data_month.index :
                mean_month.append(data_month.loc[i,month])
            acc = (month,np.mean(mean_month))
            mean_month =[]
            mean_month_acc.append(acc)
        txt=tk.Toplevel(top1)
        txt.geometry("800x200+10+10")
        tt1=tk.Message(txt,text='Mean accidents per state',relief=tk.RAISED,anchor=tk.W,width=500)
        tt1.pack(padx=10,pady=5)
        tt2=tk.Message(txt,text=mean_month_acc,relief=tk.RAISED,anchor=tk.W,width=800)
        tt2.pack(padx=10,pady=5)

    def ab4():
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
        msg='Month of minimum accidents'
        ab_prints(msg,minvalue)

    def ab5():
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
        msg='Month of maximum accidents'
        ab_prints(msg,maxvalue)

    def ab6():
        data = pd.read_csv('only_road_accidents_data3.csv')
        e= []
        cnt2 = 0
        for year in data['YEAR'].unique():
            for i in data.index:
                if data.loc[i,'YEAR'] == year:
                    cnt2 = cnt2 + data.loc[i,'Total'] 
            year_acc = (year,cnt2)
            cnt2=0
            e.append(year_acc)
        #print(c) 
        x = e[0]
        y = e[0]
        for i in e:
            if i[1]>x[1]:
                x = i
            if i[1] <y[1]:
                y=i
        msg="Year with minimum accidents:"
        ab_prints(msg,y)
        #print("Year with maximum accidents:"+ str(x))
        #print("Year with minimum accidents:" + str(y))

    def ab7():
        data = pd.read_csv('only_road_accidents_data3.csv')
        e= []
        cnt2 = 0
        for year in data['YEAR'].unique():
            for i in data.index:
                if data.loc[i,'YEAR'] == year:
                    cnt2 = cnt2 + data.loc[i,'Total'] 
            year_acc = (year,cnt2)
            cnt2=0
            e.append(year_acc)
        #print(c) 
        x = e[0]
        y = e[0]
        for i in e:
            if i[1]>x[1]:
                x = i
            if i[1] <y[1]:
                y=i
        msg="Year with maximum accidents:"
        ab_prints(msg,x)
                    
                        
    ab1=tk.Button(top1,text='Timespan of maximum accidents',width=50,height=1,command=lambda:ab_prints(msg1,x))
    ab1.pack(pady=10)

    ab2=tk.Button(top1,text='Timespan of minimum accidents',width=50,height=1,command=lambda:ab_prints(msg2,y))
    ab2.pack(pady=10)

    ab3=tk.Button(top1,text='Mean accidents per state',width=50,height=1,command=ab3)
    ab3.pack(pady=10)

    ab4=tk.Button(top1,text='Month of minimum accidents',width=50,height=1,command=ab4)
    ab4.pack(pady=10)

    ab5=tk.Button(top1,text='Month of maximum accidents',width=50,height=1,command=ab5)
    ab5.pack(pady=10)

    ab6=tk.Button(top1,text='Year of minimum accidents',width=50,height=1,command=ab6)
    ab6.pack(pady=10)

    ab7=tk.Button(top1,text='Year of maximum accidents',width=50,height=1,command=ab7)
    ab7.pack(pady=10)


    ab0=tk.Button(top1,text='Back',width=10,height=2,command=top1.destroy)
    ab0.pack(pady=10)
    top1.mainloop()
    
def predict():
    year=0
    time=0
    state=0
    top2=tk.Toplevel(r)
    top2.geometry('500x500+30+30')
    top2.title('Prediction')

    def pb_prints(msg,a):
        #tk.messagebox.showinfo(msg,a)
        
        txt=tk.Toplevel(top2)
        txt.geometry("500x100+10+10")
        tt1=tk.Message(txt,text=msg,relief=tk.RAISED,anchor=tk.W,width=300)
        tt1.pack(padx=10,pady=5)
        tt2=tk.Message(txt,text=a,relief=tk.RAISED,anchor=tk.W,width=200)
        tt2.pack(padx=10,pady=5)
        #text=tk.Text(txt)
        #text.insert(tk.END,msg)
        #text.insert(tk.END,a)
        #text.pack()    
    
    def entry(z):
        year = int(z.get())
        acc_year=model.predict(year)
        pb_prints('Predicted number of accidents',acc_year[0])
        
    def pb1():
        txt=tk.Toplevel(top2)
        txt.geometry("500x100+10+10")
        tt1=tk.Message(txt,text='Enter the Year to Predict number of Accidents',relief=tk.RAISED,anchor=tk.W,width=300)
        tt1.pack(padx=10,pady=5)
        z = tk.Entry(txt)
        z.pack()
        z.focus_set()
        b = tk.Button(txt,text='Predict',command=lambda:entry(z),activeforeground='red',width=50,height=2)
        b.pack(side='bottom')

    
    def entry1(z1,z2,z3):
        year = int(z1.get())
        state = z2.get()
        time = z3.get()
        state1=le1.transform([state])
        if time== '0-3 hrs. (Night)':
             time = 0
        elif time== '3-6 hrs. (Night)':
             time = 1
        elif time== '6-9 hrs (Day)':
             time = 2
        elif time== '9-12 hrs (Day)':
             time = 3
        elif time== '12-15 hrs (Day)':
             time = 4
        elif time== '15-18 hrs (Day)':
             time = 5
        elif time== '18-21 hrs (Night)':
             time = 6
        elif time== '21-24 hrs (Night)':
             time = 7
        cal = ohe.transform([[state1,year,time]])     
        res=model1.predict(cal)
        if res[0] < 0:
            res[0]=0
        pb_prints('Predicted number of accidents',res[0])
        
    def entry2(z1,z2,z3):
        year = int(z1.get())
        state = z2.get()
        month = z3.get()
        
        state = le_month_1.transform([state])
        month = le_month_2.transform([month])
        cal = ohe_month.transform([[state,year,month]])
        res=model3.predict(cal)
        if res[0] < 0:
            res[0]=0
        pb_prints('Predicted number of accidents',res[0])
        
    def pb2():
        txt=tk.Toplevel(top2)
        txt.geometry("800x300+10+10")
        txt.title('Multipe Linear Regression')
        
        tt1=tk.Message(txt,text='Enter the Year',relief=tk.RAISED,anchor=tk.W,width=300)
        tt1.pack(padx=10,pady=5)
        z1 = tk.Entry(txt)
        z1.pack()
        z1.focus_set()
       # year = int(z1.get())

        tt2=tk.Message(txt,text='Enter the State',relief=tk.RAISED,anchor=tk.W,width=300)
        tt2.pack(padx=10,pady=5)
        z2 = tk.Entry(txt)
        z2.pack()
        z2.focus_set()
        #state = z2.get()

        tt3=tk.Message(txt,text='Enter the Timespan',relief=tk.RAISED,anchor=tk.W,width=300)
        tt3.pack(padx=10,pady=5)
        z3 = tk.Entry(txt)
        z3.pack()
        z3.focus_set()
        #time = z3.get()
        b = tk.Button(txt,text='Predict',command=lambda:entry1(z1,z2,z3),activeforeground='red',width=50,height=2)
        b.pack(side='bottom')

    def pb3():
        txt=tk.Toplevel(top2)
        txt.geometry("800x300+10+10")
        txt.title('Multipe Linear Regression')
        
        tt1=tk.Message(txt,text='Enter the Year',relief=tk.RAISED,anchor=tk.W,width=300)
        tt1.pack(padx=10,pady=5)
        z1 = tk.Entry(txt)
        z1.pack()
        z1.focus_set()
       # year = int(z1.get())

        tt2=tk.Message(txt,text='Enter the State',relief=tk.RAISED,anchor=tk.W,width=300)
        tt2.pack(padx=10,pady=5)
        z2 = tk.Entry(txt)
        z2.pack()
        z2.focus_set()
        #state = z2.get()

        tt3=tk.Message(txt,text='Enter the Month',relief=tk.RAISED,anchor=tk.W,width=300)
        tt3.pack(padx=10,pady=5)
        z3 = tk.Entry(txt)
        z3.pack()
        z3.focus_set()
        #time = z3.get()
        b = tk.Button(txt,text='Predict',command=lambda:entry2(z1,z2,z3),activeforeground='red',width=50,height=2)
        b.pack(side='bottom')

         
        
        
        
        
    pb1=tk.Button(top2,text='Simple Linear Regression',width=50,height=1,command=pb1)
    pb1.pack(pady=10)

    pb2=tk.Button(top2,text='Multiple Linear Regression(time)',width=50,height=1,command=pb2)
    pb2.pack(pady=10)

    pb3=tk.Button(top2,text='Multiple Linear Regression(month)',width=50,height=1,command=pb3)
    pb3.pack(pady=10)
        
    pb0=tk.Button(top2,text='Back',width=10,height=2,command=top2.destroy)
    pb0.pack(pady=10)

    
    top2.mainloop()    
    
button1 = tk.Button(r,text='Analysis',width=50,height=10,command=analysis)
button1.pack(pady=10)

button2= tk.Button(r,text='Prediction',width=50,height=10,command=predict)
button2.pack(pady=10)

button3= tk.Button(r,text='Exit',width=50,height=10,command=r.destroy)
button3.pack(pady=10)

r.mainloop()
