#Number of bytes occupied by the array.
import numpy as np
a= np.array([
    [10, 20, 30],
    [40, 50, 60]
   ])
print("Number of bytes occupied by an array before reducing dtype: ",a.itemsize)
a=a.astype(np.int32)
print("Number of bytes occupied by an  after reducing dtype int32: ",a.itemsize)