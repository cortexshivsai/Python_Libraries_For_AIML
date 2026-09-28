#Find the maximum value of each column.
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Maximum value column-wie: ",np.max(data,axis=0))