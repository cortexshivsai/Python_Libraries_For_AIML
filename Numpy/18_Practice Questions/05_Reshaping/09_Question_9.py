#Swap two axes
import numpy as np
arr = np.arange(1, 25).reshape(4,6)
print("Before Converting:\n",arr)
print("Swapping Axes:\n",np.swapaxes(arr,0,1))