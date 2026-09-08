import numpy as np
# #Example 1
# a=np.arange(12).reshape(4,3)
# b=np.arange(3)
# print("Array A:\n",a)
# print("Array B:\n",b)
# print("Addition of two different arrays:\n",a+b)

# #Example 2
# a1=np.arange(12).reshape(3,4)
# b1=np.arange(3).reshape(3)
# print("Array A:\n",a1)
# print("Array B:\n",b1)
# print("Addition of two different arrays:\n",a1+b1)

# #Example 3
# a2=np.arange(3).reshape(1,3)
# b2=np.arange(3).reshape(3,1)
# print("Array A:\n",a2)
# print("Array B:\n",b2)
# print("Addition of two different arrays:\n",a2+b2) #This will throw an error cause broadcating cannot be done on these arrays

# #Example 4
# a3=np.array([1])
# b3=np.arange(4).reshape(2,2)
# print("Array A:\n",a3)
# print("Array B:\n",b3)
# print("Addition of two different arrays:\n",a3+b3)

# #Example 5
# a4=np.arange(12).reshape(3,4)
# b4=np.arange(12).reshape(4,3)
# print("Array A:\n",a4)
# print("Array B:\n",b4)
# print("Addition of two different arrays:\n",a4+b4)

#Example 6
a5=np.arange(16).reshape(4,4)
b5=np.arange(4).reshape(2,2)
print("Array A:\n",a5)
print("Array B:\n",b5)
print("Addition of two different arrays:\n",a5+b5)