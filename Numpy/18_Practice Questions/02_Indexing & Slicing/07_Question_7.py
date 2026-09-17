#Extract the first two rows.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("First 2 rows:\n ",a[0:2,0:])