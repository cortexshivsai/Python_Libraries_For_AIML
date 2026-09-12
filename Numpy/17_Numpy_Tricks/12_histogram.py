import numpy as np
a=np.random.randint(1,100,20)
print("1D Array is:\n",a)
print("Histogram No.of values in bins:\n",np.histogram(a,bins=[10,20,30,40,50,60,70,80,90,100]))
print("Histogram No.of values in bins:\n",np.histogram(a,bins=[0,50,100]))