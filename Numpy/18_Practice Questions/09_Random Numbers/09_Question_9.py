#Generate random student marks
import numpy as np
rng = np.random.default_rng()
marks = rng.integers(0, 101, size=100)
print(marks)