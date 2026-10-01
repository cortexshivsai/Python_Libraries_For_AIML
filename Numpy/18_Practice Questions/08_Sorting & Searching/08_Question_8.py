#Find where a particular value should be inserted while maintaining order
import numpy as np
scores = np.array([72, 91, 45, 88, 63, 99, 54])
scores = np.sort(scores)
print("Array before inserting value: ",scores)
index = np.searchsorted(scores, 80)
print("A particular value should be inserted while maintaining order at index: ",index)