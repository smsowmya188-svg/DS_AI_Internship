import numpy as np
x=np.array([[60,70,80],[70,80,90],[70,80,90]])
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("multiplication of two arrays:\n",np.dot(x,y))
print("\nTranspose of X:\n",x.T)
print("\nDeterminant of Y:\n",np.linalg.det(y))
print("\nInverse of Y:\n",np.linalg.inv(y))

