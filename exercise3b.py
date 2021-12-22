#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
x=["JAVA","PYTHON","PHP","JAVASCRIPT","C#","C++"]
y=[22.2,17.6,8.8,8,77,6.7]
plt.bar(x,y)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
x=["JAVA","PYTHON","PHP","JAVASCRIPT","C#","C++"]
y=[22.2,17.6,8.8,8,77,6.7]
plt.barh(x,y,color="red")
plt.show()


# In[10]:


import matplotlib.pyplot as plt
x=["JAVA","PYTHON","PHP","JAVASCRIPT","C#","C++"]
y=[22.2,17.6,8.8,8,77,6.7]
c=("pink","yellow","purple","green","blue","cyan")
plt.bar(x,y,color=c)
plt.show()


# In[15]:


import numpy as np
import matplotlib.pyplot as plt

y1=[22,30,35,35,26]
y2=[25,32,30,35,29]
x1=np.arange(5)

w=0.4
plt.bar(x1-0.2,y1,color="green",width=w,label="Men")
plt.bar(x1+0.2,y2,color="red",width=w,label="Women")

x_labels=['G1','G2','G3','G4','G5']
plt.xticks(x1,x_labels)

plt.xlabel("Person")
plt.ylabel("Scores")
plt.legend()
plt.title("Scores by group and gender")
plt.show()


# In[19]:


import numpy as np
import matplotlib.pyplot as plt

y=np.array([22.2,17.6,8.8,8,77,6.7])
l=["JAVA","PYTHON","PHP","JAVASCRIPT","C#","C++"]
plt.pie(y,labels=l)
plt.show()


# In[27]:


import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("data2.csv")
a=data["country"]
b=data["gold_medal"]

plt.pie(b,labels=a)
plt.title("Gold medal achievements of five most sucessful \n"+"countries in 2016 summer olympics")
plt.show()


# In[30]:


import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range,math_marks,label=math_marks)
plt.scatter(marks_range,science_marks,label=science_marks)

plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.show()


# In[ ]:




