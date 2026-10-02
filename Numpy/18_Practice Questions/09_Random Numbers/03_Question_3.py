#Generate 1000 random values from a normal distribution
import numpy as np
rng = np.random.default_rng()
values = rng.normal(size=1000)
print(values)