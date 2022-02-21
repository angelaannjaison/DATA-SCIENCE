#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_iris

iris = load_iris()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target, test_size=0.3,random_state=1)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred=reg.predict(X_test)
print("Accuracy:",reg.score(X_train, y_train))

sam=[[1,2,2,1]]
y=reg.predict(sam)

x=[int(each) for each in y]
p=[iris.target_names[p] for p in x]
print(p)


# In[ ]:




