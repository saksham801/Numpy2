import numpy as np

# Horizontal Splitting 

a3 = np.arange(16).reshape(4,4)
print(a3)

print(np.hsplit(a3,2))


# Vertical Spliiting

print(np.vsplit(a3,2))