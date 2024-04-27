import numpy as np
a = np.array([[[1,3,2]]])
print(a)
print(a.ndim)
b = np.array(2 ,ndmin = 30)
print(b)
print(b.ndim)
a = np.array([1,2,3,4,5, 6])
print(a.ndim)
p = a.reshape(2,-1,3)
print(p)
######################################################################################Password Genrator######################################################################################
import numpy as np
import random as rd
number = np.arange(101)
alphabet = np.array(['A','B','C','D'])
special = np.array(["@","!","$","#"])
# leng = int(input("Enter the length of string: "))
# leng1 = leng/3
# leng1 = int(leng1)
empty = []
for i in range(18):
    b = rd.choice(alphabet)
    c = rd.choice(special)
    e = rd.choice(number)
    empty.append(b)
    empty.append(c)
    empty.append(e)
ara = str(empty)
print(ara.strip())
