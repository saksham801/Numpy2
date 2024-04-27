# Reshaping
import numpy as np

# Reshape
a3 = np.arange(27).reshape(3,3,3)
print(a3)

# Transpose

transpose_a3 = np.transpose(a3)
print(transpose_a3)

# using T 

a1 = np.arange(12).reshape(3,4)
print(a1)
print(a1.T)


# Ravel convert multi dimensional to 1D dimesional

print(a3.ravel())