# arange :- use for creating Array 

import numpy as np

# arange i similar like range in python has start (including) stop (excluding) and skip
a = np.arange(1,11)
print(a)

# for skip
b = np.arange(1,11,2)
print(b)


c = np.arange(10,1,-1)
print(c)


# with reshape
# use to reshape the array in m*n ways
reshape_array = np.arange(1,13).reshape(6,2)
print(reshape_array)

