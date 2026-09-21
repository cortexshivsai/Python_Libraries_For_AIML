#Find students who scored below 40.
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Indexes of Marks Scored less than 40:\n",np.where(marks<40))
print("Marks Scored less than 40:\n",marks[np.where(marks<40)])