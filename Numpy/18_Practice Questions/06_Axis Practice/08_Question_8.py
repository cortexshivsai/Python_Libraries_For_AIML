#Find Index of maximum value in each row
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Index of maximum value in each row:")
print(np.argmax(data, axis=1))