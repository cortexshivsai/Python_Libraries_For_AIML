import numpy as np
a=np.random.randint(1,100,15)
print("Array is:\n",a)

print("All indices where values>50:\n",np.where(a>50))
print("Replace all values>50 with 0:\n",np.where(a>50,0,a))
print("Replace all even values with 0:\n",np.where(a%2==0,0,a))
