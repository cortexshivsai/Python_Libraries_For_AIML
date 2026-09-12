import numpy as np
a=np.random.randint(1,100,20)
print("1D Array is:\n",a)
print("Array After Deleting some items:\n",np.delete(a,[0,1]))
