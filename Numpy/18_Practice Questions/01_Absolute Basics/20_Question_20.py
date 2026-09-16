#Why does NumPy use a fixed data type for an array?
import numpy as np
print("WHY NUMPY USES FIXED DATA TYPES:\n")

print("""
1. Every element has a common data type.
2. NumPy knows exactly how much memory each element needs.
3. Data can be stored efficiently in contiguous memory.
4. Numerical operations can be highly optimized.
5. Vectorized operations become fast.
6. Memory usage is predictable.
7. Different dtypes allow us to choose memory vs precision.
""")

# Fixed data type
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print("dtype:", arr.dtype)
print("Memory:", arr.nbytes, "bytes")

# Specific dtype
arr32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arr64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)

print("int32 memory:", arr32.nbytes)
print("int64 memory:", arr64.nbytes)

# Type conversion
float_arr = arr.astype(np.float64)
print(float_arr)
print(float_arr.dtype)

# Vectorized operation
print(arr * 2)