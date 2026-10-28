# With one column 
import numpy as np
import pandas as pd
a=pd.read_csv("subs.csv")
print(a)
print(type(a))
a=pd.read_csv("subs.csv").squeeze("columns")
print(a,type(a))
