#Convert it into a 2×3×4 array.
import numpy as np
arr = np.arange(1, 25)
print("Before Converting:\n",arr)
print("After Converting:\n",arr.reshape(2,3,4))