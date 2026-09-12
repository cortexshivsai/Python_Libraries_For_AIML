import numpy as np
a=np.random.randint(1,100,20)
print("1D Array is:\n",a)
print("Put:\n",np.put(a,[0,1],[110,530]))
print("Updated 1D Array is:\n",a)
