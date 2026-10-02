#Generate a 5×5 matrix of random numbers
import numpy as np
rng = np.random.default_rng()
matrix = rng.integers(1, 101, size=(5, 5))
print(matrix)