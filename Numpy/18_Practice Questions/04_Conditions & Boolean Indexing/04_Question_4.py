#Replace all marks below 40 with 40.
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Marks Scored less than 40 replaced by 40:\n",np.where(marks<40,40,marks))
