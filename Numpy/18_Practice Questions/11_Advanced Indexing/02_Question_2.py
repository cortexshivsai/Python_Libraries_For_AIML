#Select specific elements without a loop
# We Want
# (0,0)
# (1,2)
# (2,4)
# (3,1)
# (4,3)
import numpy as np
a = np.arange(25).reshape(5, 5)
rows = [0, 1, 2, 3, 4]
cols = [0, 2, 4, 1, 3]
print(a[rows, cols])