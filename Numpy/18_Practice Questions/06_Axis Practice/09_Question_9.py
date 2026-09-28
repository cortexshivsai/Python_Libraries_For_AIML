#Find Index of maximum value in each column
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Index of maximum value in each column:")
print(np.argmin(data, axis=0))