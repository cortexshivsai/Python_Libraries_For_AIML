#Reverse the rows.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("Reversed Rows:\n ",a[::-1])