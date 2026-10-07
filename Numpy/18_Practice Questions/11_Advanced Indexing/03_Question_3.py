#Select all elements greater than the mean
import numpy as np
a = np.array([10, 20, 30, 40, 50])
mean = np.mean(a)
print(mean)
print(a[a > mean])
print(a[a > np.mean(a)])