import numpy as np
a=np.random.randint(1,100,24).reshape(6,4)

print("Array is:\n",a)
print("To get all numbers greater than 50:\n",a[a>50])
print("To get all even numbers:\n",a[a%2==0])
print("To get all numbers greater than 50 and even:\n",a[(a>50) & (a%2==0)])
print("To get numbers not divisible  by 7:\n",a[a%7!=0])
print("To get numbers not divisible  by 7:\n",a[~(a%7==0)])


