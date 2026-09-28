#Calculate the sum of each row.
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Sum row-wie: ",np.sum(data,axis=1))