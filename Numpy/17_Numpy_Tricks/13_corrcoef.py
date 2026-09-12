import numpy as np
salary=np.array([20000,25000,40000,60000,35000,50000])
exp=np.array([1,2,3,5,2,3])
print("Correlation:\n",np.corrcoef(exp,salary))