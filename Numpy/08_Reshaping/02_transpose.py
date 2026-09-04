import numpy as np
a2=np.arange(15).reshape(3,5)
print(a2)
#Method 1
print(np.transpose(a2))
#Method 2
# print(a2.T)