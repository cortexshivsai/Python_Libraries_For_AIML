#Replace all elements in the middle row with 0
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
a[2]=0
print("Middle elements replaced by 0:\n ",a)