#Extract diagona;.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("Diagonal Elements:\n ",np.diag(a))