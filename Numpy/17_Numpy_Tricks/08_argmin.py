import numpy as np
a=np.random.randint(1,100,15)
b=np.arange(15).reshape(3,5)
print("1D Array is:\n",a)
print("Minimum Element index in 1D array using argmin:\n",np.argmin(a))
print("2D Array is:\n",b)
print("Minimum Element index in 2D array column-wise using argmin:\n",np.argmin(b,axis=0))
print("Minimum Element index in 2D array row-wise using argmin:\n",np.argmin(b,axis=1))