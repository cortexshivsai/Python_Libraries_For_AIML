#Add different taxes to three product categories.
import numpy as np
prices = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

tax = np.array([0.05, 0.10, 0.18])
final_prices = prices + (prices * tax)
print("Final prices after tax:\n", final_prices)