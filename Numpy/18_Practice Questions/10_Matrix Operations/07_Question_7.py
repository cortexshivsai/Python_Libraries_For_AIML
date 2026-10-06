#Find eigenvectors
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
eigenvalues, eigenvectors = np.linalg.eig(a)
eigenvalues1, eigenvectors1 = np.linalg.eig(b)
print(f"Eigen Values of A:{eigenvalues}\n Eigen Vectors of A:\n{eigenvectors}")
print(f"Eigen Values of B:{eigenvalues1}\n Eigen Vectors of B:\n{eigenvectors1}")
