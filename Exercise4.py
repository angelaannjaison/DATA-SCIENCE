#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Write a python program to implement List-to-Series Conversion.
import pandas as pd
x=pd.Series(['python','java','c'])
print(x)


# In[3]:


#2.Write a python program to Generate the series of dates from 1st May, 2021 to 12th May, 2021 (both inclusive)

import pandas as pd
date_series=pd.date_range(start='05-01-2021',end='05-12-2021')
print(date_series)


# In[5]:


import pandas as pd
dict={'Name':['Anu','Anju','Nisy'],'Roll_no':[1,2,3],'Dept':['CS','MCA','CS']}
pf=pd.DataFrame(dict)
print(pf)


# In[7]:


#4.Given a 2D List, convert it into corresponding dataframe and display it
import pandas as pd
lists=[[111,'Peter',22],
       [222,'Lilly',22],
       [333,'Harry',22]]
dataframe=pd.DataFrame(lists,columns=['id','name','age'])
print(dataframe)


# In[12]:


#5.Given a CSV file, read it into a dataframe and display it.

import pandas as pd
df=pd.read_csv('ex4_data.csv')
print(df)


# In[10]:


#6.Given a dataframe, sort it by multiple columns.
import pandas as pd
dict={'ID':[111,222,111],'Name':['Anju','Anu','Lilly'],'Age':[23,22,24]}
df=pd.DataFrame(dict)
print(df)
print("After sorting")
sort=df.sort_values(by=['ID','Age'])
print(sort)


# In[12]:


#7.Given a dataframe with custom indexing, convert and it to default indexing and display it
import pandas as pd
data={'Name':['Anju','Anu','Lilly'],'Rollno':[1,2,3],'Dept':['CS','CS','MCA']}
df=pd.DataFrame(data,index=['a','b','c'])
print(df)
df.reset_index(inplace=True,drop=True)
print(df)


# In[19]:


#8. Given a dataframe, select first 2 rows and output them.
import pandas as pd
data={'Name':['Arjun','Amal','Lakshmi'],'Rollno':[1,2,3],'Dept':['CS','CS','MCA']}
df=pd.DataFrame(data)
print(df)
print("-----------extracting first 2 rows-----------")
df1=df.head(2)
print(df1)


# In[23]:


#9.Given is a dataframe showing name, occupation, salary of people. Find the average salary per occupation.
import pandas as pd

data={'Name':['Tom','Cyril','Nayana','Sanoop','Maya'],
      'Occupation':['Engineer','Bank Manager','Teacher','Engineer','Teacher'],
      'Salary':[45000,60000,35000,55000,20000]}
df=pd.DataFrame(data)
print(df)
print("------------------------average salary per occupation--------------------------")
avg_sal=df.groupby('Occupation')['Salary'].mean()
print(avg_sal)


# In[28]:


#10.Given a dataframe with NaN Values, fill the NaN values with 0.
import pandas as pd
import numpy as np

data={'id':[1,2,3],'Name':['Charlie','Manasa','Sandeep'],'Phone':[np.nan,32942332,np.nan]}
df=pd.DataFrame(data)
print(df)
print("-----------------------After filling the NaN values with 0-----------------")
fill=df.fillna(0)
print(fill)


# In[35]:


#11. Given is a dataframe showing Company Names (cname) and corresponding Profits (profit). 
#Convert the values of Profit column such that values in it greater than 0 are set to True 
#and the rest are set to False.
import pandas as pd
data={'Name':['ABC','DEF','GHI'],'Profit':[-2000,10000,30000]}
df=pd.DataFrame(data)
print(df)
print("--------------------------Setting values greater than 0 True and vise versa -------------------")
df['Profit']=df['Profit'].apply(lambda x:x>0)
print(df)


# In[37]:


#12. Given are 2 dataframes, with one dataframe containing Employee ID (eid), Employee
#Name (ename) and Stipend (stipend) and the other dataframe containing Employee ID
#(eid) and designation of the employee (designation). Output the Dataframe containing
#Employee ID (eid), Employee Name (ename), Stipend (stipend) and Position (position).

import pandas as pd
data1={'eid':[1,2,3],
      'ename':['Sagar','Akash','Manu'],
       'stipend':[3000,2000,5000]}
data2={'eid':[1,2,3],
      'designation':['Salesman','Sales Executive','Manager']}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print("Dataframe-1")
print(df1)
print("Dataframe-2")
print(df2)
print("---------------------------------After updating-------------------------------------")
df3=pd.merge(df1,df2,how='inner',on='eid')
print(df3)


# In[ ]:




