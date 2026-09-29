#Apply a 10% discount to every price.
import numpy as np
prices = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])
print("Dscounted prices:\n",prices*0.90)