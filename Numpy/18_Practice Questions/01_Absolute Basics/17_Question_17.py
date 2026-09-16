#Create a float array and convert it to integer.
import numpy as np
a=np.arange(12,dtype=float).reshape(3,4)
print("Array before converting to integer:\n ",a)
print("Data Type of array before converting: ",a.dtype)
a=np.arange(12,dtype=int).reshape(3,4)
print("Array after converting to integer:\n ",a)
a=a.astype(np.int64)
print("Data Type of array after converting: ",a.dtype)



