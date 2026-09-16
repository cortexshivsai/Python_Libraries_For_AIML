#Compare the memory usage of int32 and int64.
import numpy as np
a=np.arange(9).reshape(3,3)
print("Memory usage of int64: ",a.itemsize)
b=a.astype(np.int32)
print("Memory usage of int32: ",b.itemsize)
