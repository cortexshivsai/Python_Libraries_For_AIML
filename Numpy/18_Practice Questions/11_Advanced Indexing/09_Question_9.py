#Find duplicate values and their positions
import numpy as np
a = np.array([10, 20, 30, 20, 40, 10, 50, 30])
unique, counts = np.unique(a, return_counts=True)
print("Values:", unique)
print("Counts:", counts)
duplicate_values = unique[counts > 1]
print("Duplicate Values are: ",duplicate_values)
for value in duplicate_values:
    positions = np.where(a == value)[0]
    print(value, "→", positions)