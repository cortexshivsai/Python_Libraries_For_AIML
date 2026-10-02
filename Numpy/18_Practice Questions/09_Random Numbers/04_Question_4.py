#Calculate their mean and standard deviation of Q3
import numpy as np
rng = np.random.default_rng()
values = rng.normal(size=1000)
print(values)
mean = np.mean(values)
std = np.std(values)
print("Mean:", mean)
print("Standard deviation:", std)