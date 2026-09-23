# Explain differnce between these
# reshape()
# flatten()
# ravel()
# resize() 
import numpy as np
arr = np.arange(1, 7).reshape(2, 3)
print("Initial Array is:\n",arr)

arr = np.arange(1, 7)
new_arr = arr.reshape(3, 2)
print("Use of reshape():\n",new_arr)

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
new_arr = arr.flatten()
print("Use of flatten():\n",new_arr)

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
new_arr = arr.ravel()
print("Use of ravel():\n",new_arr)

arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize(2, 4)
print("Use of resize():\n",arr)