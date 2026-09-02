import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)
print("Array is:\n",a1)
#For Entire Array
print("Mean for entire array is:\n",np.mean(a1))
print("Median for entire array is:\n ",np.median(a1))
print("Standard Deviation for entire array is:\n ",np.std(a1))
print("Variance for entire array is:\n ",np.var(a1))

#For a Row axis=1
print("Mean for each row is:\n ",np.mean(a1,axis=1))
print("Median for each row  is:\n ",np.median(a1,axis=1))
print("Standard Deviation for each row  is:\n ",np.std(a1,axis=1))
print("Variance for each row  is:\n ",np.var(a1,axis=1))


#For a Column axis=0

print("Mean for each column is:\n ",np.mean(a1,axis=0))
print("Median  for each column is:\n ",np.median(a1,axis=0))
print("Standard Deviation  for each column is:\n ",np.std(a1,axis=0))
print("Variance  for each column is:\n",np.var(a1,axis=0))