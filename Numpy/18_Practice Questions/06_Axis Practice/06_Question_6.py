#Find the maximum value of each row.
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Maximum value row-wie: ",np.max(data,axis=1))