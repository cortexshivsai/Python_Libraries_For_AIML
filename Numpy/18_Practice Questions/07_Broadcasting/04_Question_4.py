#Standardize every column:
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
#x_standardized = (x - mean) / std
print("Standrdized Columns:\n",(a-np.mean(a)/np.std(a)))