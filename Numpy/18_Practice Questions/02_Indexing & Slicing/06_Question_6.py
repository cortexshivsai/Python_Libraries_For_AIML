#Extract the middle 3×3 matrix.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("Middle 3*3 Matrix:\n ",a[1:4,1:4])