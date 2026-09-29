#Subtract the mean of each column from its column.
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
mean1=np.mean(a,axis=0)
print("Difference:\n",a-mean1)
