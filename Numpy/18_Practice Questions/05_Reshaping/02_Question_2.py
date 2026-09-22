#Convert it into a 6×4 matrix.
import numpy as np
arr = np.arange(1, 25)
print("Before Converting:\n",arr)
print("After Converting:\n",arr.reshape(6,4))