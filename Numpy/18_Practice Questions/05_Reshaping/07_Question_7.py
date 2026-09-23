#Add a new dimension.
import numpy as np
arr = np.arange(1, 25).reshape(4,6)
print("Before Converting:\n",arr)
print("Expanding Dimension Column-wise in Matrix:\n",np.expand_dims(arr,axis=0))
print("Expanding Dimension Row-wise in Matrix:\n",np.expand_dims(arr,axis=1))