#Replace all negative numbers with zero
import numpy as np
a = np.array([-5, 10, -3, 20, -8, 15])
a[a < 0] = 0
print(a)