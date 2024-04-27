
# Array Operations 
import numpy as np

a1 = np.arange(1,11).reshape(2,5)
print(a1)

a2 = np.arange(10,20).reshape(2,5)
print(a2)

# Scalar Operations
#arithmetic Operations
print("Addition :- ", a1+2)
print("Substracion :- ", a1-4)
print("Multplication :- ", a1 * 2)
print("Divsion :- ", a1 / 2)
print("power :- ", a1 ** 2)
print("Modulas :- ", a1 % 2)



# relational Operations

x = 5
print("Value Greater Than x :- " ,a1 > x)
print("Value less Than x :- " ,a1 < x)
print("Value less  Than eqaul x :- " ,a1 <= x)
print("Value greater  Than eqaul x :- " ,a1 >= x)
print("Value eqaul to x :- " ,a1 == x)



# Vector Operations

print("Addition :- " , a1 + a2)
print("Substraction :- " , a1 - a2)
print("Multiplication :- " , a1 * a2)
print("Division :- " , a1 / a2)
print("power :- " , a1 ** a2)
print("modulas :- " , a1 % a2)