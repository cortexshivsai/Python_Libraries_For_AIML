#Find the determinant
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
det = np.linalg.det(a)
det1=np.linalg.det(b)
print("Determinant of A:\n ",det)
print("Determinant of B:\n ",det1)