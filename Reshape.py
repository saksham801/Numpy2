# Reshape = We can edit or convert the 1-d to 2-d or any dimension
# TO use reshape = var.reshape(parmeter)
# If we have to commond that it chosse automatcialy we give the or write in parameter in -1
# If we have to check the created reshape is copy or view we use .base if it's view it return same as the created
# If we have to create multidimension array we use ndmin
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
v = a.reshape(2, 3)
print(v)
# .base
print(v.base)
