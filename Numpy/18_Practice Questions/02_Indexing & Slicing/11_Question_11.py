#Reverse Entire  Matrix.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("Reversed Matrix:\n ",a[::-1,::-1])