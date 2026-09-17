#Extract the last two columns
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("Last 2 Columns:\n ",a[0:,3:])