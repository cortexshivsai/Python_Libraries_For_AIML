#Add different taxes to three product categories
import numpy as np
data = np.random.randint(1, 101, size=(100, 3))
mean = np.mean(data, axis=0)
centered_data = data - mean
print("Shape:", data.shape)
print("Feature means:", mean)
print("Centered data:\n", centered_data)