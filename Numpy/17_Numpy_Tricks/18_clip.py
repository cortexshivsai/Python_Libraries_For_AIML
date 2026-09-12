import numpy as np
a=np.random.randint(1,100,20)
print("1D Array is:\n",a)
print("Clip:\n",np.clip(a,a_min=50,a_max=80))