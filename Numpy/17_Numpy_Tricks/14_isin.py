import numpy as np
a=np.random.randint(1,100,15)
items=[10,20,30,40,50,60,70,80,90,100]
print("1D Array is:\n",a)
print("Items isin numpy array:\n",np.isin(a,items))
print("Isin Elemnts in items:\n",a[np.isin(a,items)])