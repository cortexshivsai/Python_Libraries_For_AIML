#Simulate rolling a dice 10,000 times
import numpy as np
rng = np.random.default_rng()
dice = rng.integers(1, 7, size=10000)
print(dice)