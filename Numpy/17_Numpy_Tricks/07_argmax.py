import numpy as np
a=np.random.randint(1,100,15)
b=np.arange(15).reshape(3,5)
print("1D Array is:\n",a)
print("Maximum Element index in 1D array using argmax:\n",np.argmax(a))
print("2D Array is:\n",b)
print("Maximum Element index in 2D array column-wise using argmax:\n",np.argmax(b,axis=0))
print("Maximum Element index in 2D array row-wise using argmax:\n",np.argmax(b,axis=1))