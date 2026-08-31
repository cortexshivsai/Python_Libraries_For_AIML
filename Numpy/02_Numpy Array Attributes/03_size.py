import numpy as np
a1=np.arange(10) #1D Array
print("Array is:",a1)
b=a1.size
print("No. of Items: ",b)

a2=np.arange(20,dtype=float).reshape(5,4) #2D Array
print("Array is:\n",a2)
c=a2.size
print("No. of Items: ",c)


a3=np.arange(12).reshape(3,2,2)
print("Array is:\n",a3)
d=a3.size
print("No. of Items: ",d)
