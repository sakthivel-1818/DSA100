import math
from math import isqrt

n=100120321
print(isqrt(100120321))
for i in range(2,isqrt(n)):
    if n%i==0:
        print("not prime")
print("prime")



