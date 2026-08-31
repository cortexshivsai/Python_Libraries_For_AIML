import numpy as np
a1=np.arange(10,dtype=np.int32) #1D Array Without np.int32 it will print 8 bytes
print("Array is:",a1)
b=a1.itemsize
print("Memory Occupied in bytes: ",b)#Prints 32 bit integer output

a2=np.arange(12,dtype=float).reshape(3,4) #2D Array
print("Array is:\n",a2)
c=a2.itemsize
print("Memory Occupied in bytes: ",c)


a3=np.arange(8).reshape(2,2,2)
print("Array is:\n",a3)
d=a3.itemsize
print("Memory Occupied in bytes: ",d)
