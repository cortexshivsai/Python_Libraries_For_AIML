import numpy as np
a=np.random.randint(1,100,15)
b=np.arange(15).reshape(3,5)
print("1D Array is:\n",a)
print("Cumulative product of 1D array:\n",np.cumprod(a))
print("2D Array is:\n",b)
print("Cumulative product of 2D array column-wise:\n",np.cumprod(b,axis=0))
print("Cumulative product of 2D array row-wise:\n",np.cumprod(b,axis=1))