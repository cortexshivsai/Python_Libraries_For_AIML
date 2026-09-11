import numpy as np
a=np.random.randint(1,100,15)
print("Array is:\n",a)
print("Column-wise Expanded Dimension Array:\n",np.expand_dims(a,axis=0))
print("Row-wise Expanded Dimension Array:\n",np.expand_dims(a,axis=1))