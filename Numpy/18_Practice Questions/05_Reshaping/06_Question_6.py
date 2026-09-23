#Transpose a 4×6 matrix.
import numpy as np
arr = np.arange(1, 25).reshape(4,6)
print("Before Converting:\n",arr)
print("Transpose Matrix:\n",np.transpose(arr))