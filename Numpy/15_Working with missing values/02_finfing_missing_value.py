import numpy as np
a=np.array([1,2,3,4,np.nan,6])
print(a)
b=np.isnan(a)
print(b)

c=a[~np.isnan(a)]
print(c)