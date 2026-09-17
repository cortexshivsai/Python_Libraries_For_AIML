#Get the first column.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("First Column: ",a[0:,0])