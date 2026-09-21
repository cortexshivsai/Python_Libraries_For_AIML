#Find students who scored between 50 and 80.
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Indexes of Marks Scored between 50  80:\n",np.where((marks>=50) & (marks<=80)))
print("Marks Scored between 50  80:\n",marks[np.where((marks>=50) & (marks<=80))])