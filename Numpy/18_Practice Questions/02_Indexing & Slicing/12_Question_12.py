#Extract every second element.
import numpy as np
a= np.arange(1, 26).reshape(5, 5)
print("Array is:\n",a)
print("Every Second Element:\n ",a.flatten()[::2])