#Flatten the array
import numpy as np
arr = np.arange(1, 25)
print("Before Converting:\n",arr)
print("After Converting:\n",arr.reshape(2,3,4))
print("After Flattening:\n",arr.flatten())