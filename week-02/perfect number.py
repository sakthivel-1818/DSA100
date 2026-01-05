import math
from itertools import count
from math import isqrt
from struct import pack_into

#// perfect number
# n=28                         ##//sqrt of 28 is 5*5=25 6*6=36 so 5

# sum=1
# for i in range(2,isqrt(n)+1): ## i ==2,3,4,5
#     if n%i==0: #
#         sum+=i
#         if n//i!=i:
#             sum+=n//i  #gives 7,14,
#
# if sum==n:
#     print("perfect")
# else:
#     print("not perfect")
#
# n=9
# num=(isqrt(n))
# count=0
# while num>=1:
#     count+=1
#     num-=1
# print(count)

# n=9
# sum=0
# for i in range(1,isqrt(n)+1):
#     if i * i<n:
#         sum+=1
#     else:
#         break
# print(sum)
#
# a="2"
# b="4"
# n=pow(int(a),int(b),10)
# print(n)

n=23
temp=str(n)
count=0
for i in temp:
    if int(i)==0:
        count+=0
    elif n%int(i)==0:
        count+=1
print(count)