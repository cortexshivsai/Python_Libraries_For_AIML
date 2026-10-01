#Find unique values and their frequencies
import numpy as np
numbers = np.array([10, 20, 10, 30, 20, 40, 30, 50])
unique, counts = np.unique(numbers, return_counts=True)
print("Unique values:", unique)
print("Frequencies:", counts)