#Generate random heights for 1,000 people
import numpy as np
rng = np.random.default_rng()
heights = rng.normal(loc=170, scale=10, size=1000)
print(heights)