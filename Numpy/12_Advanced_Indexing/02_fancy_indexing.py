# Fancy Indexing
import numpy as np
a=np.arange(24).reshape(6,4)
print("Array is:\n",a)
print("To get 1st,3rd,4th & 6th row:\n",a[[0,2,3,5]])

print("To get 1st,3rd & 4th Column:\n",a[:,[0,2,3]])