import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

print("1D Array iteration of each element:\n")
for i in np.nditer(a1):
    print(i)

print("2D Array iteration of each element:\n")
for i in np.nditer(a2):
    print(i)


print("3D Array iteration of each element:\n")
for i in np.nditer(a3):
    print(i)
