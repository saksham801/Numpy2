# Horizontal Stacking

import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a1,a2)

print(np.hstack((a1,a2)))

# Vertical Stacking

print(np.vstack((a1,a2)))