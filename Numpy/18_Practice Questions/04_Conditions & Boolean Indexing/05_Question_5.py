#Count how many students scored above 75.
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Count of students Scored above 75:\n",np.sum(marks>75))
