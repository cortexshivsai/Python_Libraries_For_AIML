#Remove a dimension of size 1.
import numpy as np
arr = np.arange(1, 25).reshape(4,6)
print("Before Converting:\n",arr)
print("Expanding Dimension Column-wise in Matrix:\n",np.expand_dims(arr,axis=0))
print("Removing a dimension of size 1:\n",np.square(arr))

