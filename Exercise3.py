#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,marker='o',mec='g',mfc='g',ms='10',linestyle='dotted',color='r')
plt.show()


# In[14]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([12,14,16,18,20,22,24])
y=np.array([100,200,250,400,300,450,500])
plt.plot(x,y,marker='o',mfc='b')
plt.show()


# In[18]:


import matplotlib.pyplot as plt

with open("data1.txt") as f:
    data=f.read()
data=data.split('\n')
x=[row.split(' ')[0] for row in data]
y=[row.split(' ')[1] for row in data]
plt.plot(x,y)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('graph')
plt.show()


# In[19]:


import matplotlib.pyplot as plt
x1=([10,20,30])
y1=([20,40,50])
plt.plot(x1,y1,label='line1')

x2=([10,20,30])
y2=([40,10,30])
plt.plot(x2,y2,label='line2')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()


# In[22]:


import matplotlib.pyplot as plt

plt.subplot(1,2,1)
x1=[10,20,30]
y1=[6,2,9]
plt.title("first plot")
plt.plot(x1,y1)

plt.subplot(1,2,2)
x2=[2,4,6]
y2=[0,1,2]
plt.title("Second plot")
plt.plot(x2,y2)

plt.show()







