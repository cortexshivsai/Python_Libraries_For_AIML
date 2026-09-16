#Create an integer array and convert it to float.
import numpy as np
a=np.arange(16).reshape(4,4)
print("Array before converting to float:\n ",a)
print("Data Type of array before converting: ",a.dtype)
a=np.arange(16,dtype=float).reshape(4,4)
print("Array after converting to float:\n ",a)
print("Data Type of array after converting: ",a.dtype)


