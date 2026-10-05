#Find the inverse
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
inv = np.linalg.inv(a)
inv1=np.linalg.inv(b)
print("Inverse of A:\n ",inv)
print("Inverse of B:\n ",inv1)