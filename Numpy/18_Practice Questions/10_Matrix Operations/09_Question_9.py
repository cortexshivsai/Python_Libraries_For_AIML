#Verify the solution
import numpy as np
a=np.array([
    [2, 1],
    [1, 3]
])
b=np.array([10, 15])
solution=np.linalg.solve(a, b)
print("Values of X and Y are:\n",solution)
print("Verified Answers are:",a @ solution)