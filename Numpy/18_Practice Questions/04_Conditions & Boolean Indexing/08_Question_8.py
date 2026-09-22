#Find the lowest marks and its index
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Lowest Marks:\n",marks[np.argmin(marks)])
print("Index of Lowest Marks:\n",np.argmin(marks))

