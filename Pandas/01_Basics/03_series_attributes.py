import numpy as np
import pandas as pd

marks={
    "Maths":67,
    "English":57,
    "Science":89,
    "Marathi":100
}
c=pd.Series(marks,name="Shiv's Marks")
print(c)


# Size

print(c.size)

# dtype
print(c.dtype)


# name
print(c.name)


# is_unique
print(c.is_unique)


# index
print(c.index)


# values
print(c.values)