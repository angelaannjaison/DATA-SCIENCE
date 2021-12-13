#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
  
R1 = int(input("Enter the number of rows of matrix1:"))
C1 = int(input("Enter the number of columns of matrix1:"))
print("Enter the entries in a single line (separated by space): ")
entries1 = list(map(int, input().split()))
matrix1 = np.array(entries1).reshape(R1, C1)
print(matrix1)

R2 = int(input("Enter the number of rows of matrix2:"))
C2 = int(input("Enter the number of columns of matrix2:"))
print("Enter the entries in a single line (separated by space): ")
entries2 = list(map(int, input().split()))
matrix2 = np.array(entries2).reshape(R2, C2)
print(matrix2)

print("\n---DOT PRODUCT----\n")
print(np.dot(matrix1,matrix2))

print("\n----TRANSPOSE----\n")
print(matrix1.transpose())
print(matrix2.transpose())

print("\n----TRACE----\n")
print("Trace of matrix1=",matrix1.trace())
print("Trace of matrix2=",matrix2.trace())

print("\n----RANK----\n")
rank1=np.linalg.matrix_rank(matrix1)
print("Rank of first matrix=",rank1)
rank2=np.linalg.matrix_rank(matrix2)
print("Rank of second matrix=",rank2)

print("\n----DETERMINANT----\n")
print("Dterminant of matrix1=",np.linalg.det(matrix1))
print("Dterminant of matrix2=",np.linalg.det(matrix2))

print("\n----INVERSE----\n")
print("\nInverse of matrix1=\n",np.linalg.inv(matrix1))
print("\nInverse of matrix2=\n",np.linalg.inv(matrix2))

print("\n----EIGEN VALUES AND EIGEN VECTORS----\n")

print("\nEigen values of matrix1\n")
w1,v1=np.linalg.eig(matrix1)
print("\nEigen values:\n")
print(w1)
print("\nEigen vectors:\n")
print(v1)

print("\nEigen values of matrix2\n")
w2,v2=np.linalg.eig(matrix1)
print("\nEigen values:\n")
print(w2)
print("\nEigen vectors:\n")
print(v2)


# In[ ]:




