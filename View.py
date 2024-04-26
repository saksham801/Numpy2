# View = It get change after creating on the both variable
# If we have to add element we sholud give index
import numpy as np
a = np.array([1,2,3,4,5])
b = a.view()
print(b)
b[0]= 50
print(b)
print(a)