import numpy as np
a=np.random.randint(1,100,15)
b=np.arange(15).reshape(3,5)
print("1D Array is:\n",a)
print("Cumulative Sum of 1D array:\n",np.cumsum(a))
print("2D Array is:\n",b)
print("Cumulative Sum of 2D array column-wise:\n",np.cumsum(b,axis=0))
print("Cumulative sum of 2D array row-wise:\n",np.cumsum(b,axis=1))