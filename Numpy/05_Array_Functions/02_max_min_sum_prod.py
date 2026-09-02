import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)
print("Array is:\n",a1)
#For Entire Array
print("Minimum is: ",np.min(a1))
print("Maximum is: ",np.max(a1))
print("Sum is: ",np.sum(a1))
print("Product is: ",np.prod(a1))

#For a Row axis=1
print("Minimum is: ",np.min(a1,axis=1))
print("Maximum is: ",np.max(a1,axis=1))
print("Sum is: ",np.sum(a1,axis=1))
print("Product is: ",np.prod(a1,axis=1))


#For a Column axis=0

print("Minimum is: ",np.min(a1,axis=0))
print("Maximum is: ",np.max(a1,axis=0))
print("Sum is: ",np.sum(a1,axis=0))
print("Product is: ",np.prod(a1,axis=0))



