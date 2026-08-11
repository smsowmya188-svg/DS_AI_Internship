import numpy as np

x = np.array([[60,70,80],
              [70,80,90],
              [80,90,110]])
print("Matrix x:")
print(x)
print("\nDeterminant:")
print(np.linalg.det(x))

