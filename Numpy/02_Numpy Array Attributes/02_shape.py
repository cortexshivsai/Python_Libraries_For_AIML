import numpy as np
a1=np.arange(10) #1D Array
print("Array is:",a1)
b=a1.shape
print("Dimensions: ",b) #Tells that there are 10 elements in a single row

a2=np.arange(12,dtype=float).reshape(3,4) #2D Array
print("Array is:\n",a2)
c=a2.shape
print("Dimensions: ",c) #Tells that there are 3 rows and 4 columns


a3=np.arange(8).reshape(2,2,2)
print("Array is:\n",a3)
d=a3.shape
print("Dimensions: ",d) #Tells that there are 2 2D arrays 
