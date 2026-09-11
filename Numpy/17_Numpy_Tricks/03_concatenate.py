import numpy as np
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)
print("Array A:\n",a)
print("Array B:\n",b)
print("2D array Concatenate Column-wise:\n",np.concatenate((a,b),axis=0))
print("2D array Concatenate Row-wise:\n",np.concatenate((a,b),axis=1))