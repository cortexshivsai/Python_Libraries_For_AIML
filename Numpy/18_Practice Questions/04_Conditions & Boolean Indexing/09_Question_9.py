# Convert marks into:
# 1 if marks ≥ 50
# 0 otherwise.
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Marks Conversion into 1 and 0:\n",np.where(marks<=50,1,0))
