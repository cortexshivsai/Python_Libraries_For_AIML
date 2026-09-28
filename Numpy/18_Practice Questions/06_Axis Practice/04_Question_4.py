#Calculate the mean of each row.
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Mean row-wie: ",np.mean(data,axis=1))