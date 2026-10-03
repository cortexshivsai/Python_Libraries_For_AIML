#Simulate 1,000 coin tosses
import numpy as np
rng = np.random.default_rng()
coin = rng.integers(0, 2, size=1000)
print(coin)