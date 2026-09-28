#Normalize each column.
import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
column_min = data.min(axis=0)
column_max = data.max(axis=0)

normalized = (data - column_min) / (column_max - column_min)

print(normalized)