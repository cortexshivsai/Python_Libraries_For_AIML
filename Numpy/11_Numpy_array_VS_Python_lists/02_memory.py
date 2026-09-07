import sys
import numpy as np
# FOr Lists
a=[i for i in range(10000000)]
print("Memory Occupied by list in bytes: ",sys.getsizeof(a))

b=np.arange(10000000)
print("Memory Occupied by numpy before reducing int data type in bytes: ",sys.getsizeof(b))

c=np.arange(10000000,dtype=np.int32)
print("Memory Occupied by numpy after reducing int data type to int32 in bytes: ",sys.getsizeof(c))


c=np.arange(10000000,dtype=np.int16)
print("Memory Occupied by numpy after reducing int data type to int16 in bytes: ",sys.getsizeof(c))


c=np.arange(10000000,dtype=np.int8)
print("Memory Occupied by numpy after reducing int data type to int8 in bytes: ",sys.getsizeof(c))
