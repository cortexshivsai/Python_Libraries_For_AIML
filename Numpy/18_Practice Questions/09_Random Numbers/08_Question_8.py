#Estimate the probability of getting heads of Q7
import numpy as np
rng = np.random.default_rng()
coin = rng.integers(0, 2, size=1000)
print(coin)
probability_heads = np.mean(coin)
print("Estimated probability of heads:", probability_heads)