#Find eigenvalues
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
eigenvalues1 = np.linalg.eigvals(a)
eigenvalues2 = np.linalg.eigvals(b)
print("Eigen Values of A:\n ",eigenvalues1)
print("Eigen Values of B:\n ",eigenvalues2)