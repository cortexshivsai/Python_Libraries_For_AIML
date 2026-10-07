#Replace all values greater than 100 with 100
import numpy as np
a = np.array([50, 120, 80, 150, 90, 200])
a[a > 100] = 100
print(a)