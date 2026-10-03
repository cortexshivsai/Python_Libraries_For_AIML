#Set a random seed and verify reproducible results
import numpy as np
rng = np.random.default_rng(42)
numbers1 = rng.integers(1, 101, size=10)
print(numbers1)
rng = np.random.default_rng(42)
numbers2 = rng.integers(1, 101, size=10)
print(numbers2)
print(np.array_equal(numbers1, numbers2))