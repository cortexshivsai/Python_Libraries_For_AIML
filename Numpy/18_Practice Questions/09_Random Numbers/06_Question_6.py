#Calculate the frequency of each dice result of Q5
import numpy as np
rng = np.random.default_rng()
dice = rng.integers(1, 7, size=10000)
print(dice)
frequency = np.bincount(dice)[1:]
print("Frequency: ",frequency)
