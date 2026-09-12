import numpy as np
a=np.random.randint(1,100,15)
b=np.arange(15).reshape(3,5)
print("1D Array is:\n",a)
print("Flip of 1D array:\n",np.flip(a))
print("2D Array is:\n",b)
print("Flip of 2D array column-wise:\n",np.flip(b,axis=0))
print("Flip of 2D array row-wise:\n",np.flip(b,axis=1))
print("Flip of 2D array column-wise and row-wise:\n",np.flip(b))