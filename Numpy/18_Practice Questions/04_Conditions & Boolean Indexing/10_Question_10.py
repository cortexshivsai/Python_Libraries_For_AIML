# Use np.where() to assign grades:
# A ≥ 80
# B ≥ 60
# C ≥ 40
# F < 40
import numpy as np
marks = np.array([45, 78, 32, 90, 66, 51, 28, 84, 73, 39])
print("Grade assigned for marks>=80 & marks<=100:\n",np.where((marks>=80) & (marks<=100),"A",marks))
print("Grade assigned for marks>=60 & marks<80:\n",np.where((marks>=60) & (marks<80),"B",marks))
print("Grade assigned for marks>=40 & marks<60:\n",np.where((marks>=40) & (marks<60),"C",marks))
print("Grade assigned for marks<40:\n",np.where(marks<40,"F",marks))

