import numpy as np
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])
result=np.concatenate((x,y) ,axis=1)
print(result)