import numpy as np
a1=np.arange(10)#1D Array
a2=np.arange(12).reshape(3,4)#2D Array
a3=np.arange(27).reshape(3,3,3) #3D Array
print("1D Array is:\n",a1)
print("2D array is:\n",a2)
print("3D array is:\n",a3)

print("1D array slicing:\n",a1[2:5]) #Slicing in 1D array
print("1D array slicing with step size of 2:\n",a1[2:5:2]) #Slicing in 1D array with step size of 2

print("2D array slicing:\n",a2[1:3, 0:2]) #Slicing in 2D array
print("0th row:\n",a2[0,:])#Gives whole 0th row consisting of every column
print("3rd Column:\n",a2[:,2])#Gives whole 2nd column consisting of every row
print("To get 5,6 & 9,10:\n",a2[1: ,1:3])#It gives the only 5,6 and 9,10 these elements
print("To get 0,3 & 8,11:\n ",a2[::2,::3])#It gives 0,3 and 8,11  all corner elements 
print("To get 1,3 & 9,11:\n",a2[::2,1::2])#iT GIVES 1,3 AND 9,11
print("To get 4,7:\n",a2[1,::3])
print("To get 1,2,3 & 5,6,7:\n",a2[0:2,1:])

print("3D array Slicing:\n",a3)
print("To get middle matrix of a 3D array:\n",a3[1])
print("To get first and last matrix of a 3D array:\n",a3[::2])
print("To get first matrix  second row of a 3D array:\n",a3[0,1,:])
print("To get second matrix middle column of a 3D array:\n",a3[1,:,1])
print("To get last matrix 22,23 & 25,26 of a 3D array:\n",a3[2,1:,1:])
print("To get 0,2 from first matrix and 18,20 from last matrix of a 3D array:\n",a3[::2,0,::2])




