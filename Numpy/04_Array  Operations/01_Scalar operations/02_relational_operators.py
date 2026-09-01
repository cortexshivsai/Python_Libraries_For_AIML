import numpy as np
a1=np.arange(15).reshape(5,3)
a2=np.arange(10,30).reshape(4,5)
print("Before using relational operator  on a1:\n",a1)
print("After using relational operator ( > ) on a1:\n",a1>25)
print("After using relational operator ( >= ) on a1:\n",a1>=21)
print("After using relational operator ( < ) on a1:\n",a1<12)
print("After using relational operator ( <= ) on a1:\n",a1<=34)
print("After using relational operator ( == ) on a1:\n",a1==13)

print("Before using relational operator  on a2:\n",a2)


print("After using relational operator ( > ) on a2:\n",a2>27)
print("After using relational operator ( >= ) on a2:\n",a2>=90)
print("After using relational operator ( < ) on a2:\n",a2<32)
print("After using relational operator ( <= ) on a2:\n",a2<=13)
print("After using relational operator ( == ) on a2:\n",a2==43)
