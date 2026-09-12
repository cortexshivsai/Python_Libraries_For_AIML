import numpy as np
a=np.random.randint(1,100,15)
print("1D Array is:\n",a)
print("Percentile close to 100:\n",np.percentile(a,100))
print("Percentile close to 0:\n",np.percentile(a,0))
print("Average Percentile:\n",np.percentile(a,50))


