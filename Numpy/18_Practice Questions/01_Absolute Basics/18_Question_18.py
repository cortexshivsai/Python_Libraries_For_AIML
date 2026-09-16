#Create an array using int32.
import numpy as np
a=np.arange(12).reshape(3,4)
b=a.astype(np.int32)
print(b)
print(b.dtype)