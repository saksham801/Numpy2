# Iterating array

import numpy as np

a1 = np.arange(10)
print(a1)

for i in a1:
    print(i)


a2 = np.arange(12).reshape(3,4)
print(a2)

for i in a2:
    print(i)


a3 = np.arange(27).reshape(3,3,3)
print(a3)

for i in a3:
    print(i)


# np.nditer :- use to iterte thourgh each and every eleement present in varaible

for i in np.nditer(a3):
    print(i)