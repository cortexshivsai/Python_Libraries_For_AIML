#Find the top 3 scores
import numpy as np
scores = np.array([72, 91, 45, 88, 63, 99, 54])
print("Top 3 scores are: ",np.sort(scores)[-3:][::-1])
