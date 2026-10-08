#Extract the lower triangular portion
import numpy as np
a = np.arange(1, 10).reshape(3, 3)
print("Array is: \n",a)
print("Lower Triangular Portion:\n",np.tril(a))