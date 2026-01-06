from math import isqrt
# n=20
# a=[0]*(n+1)
# for i in range(2,isqrt(n)+1):
#     if a[i]==0:
#         for j in range(i*2,n+1,i):
#             a[j]=1
#
# for i in range(2,n+1):
#     if a[i]==0:
#         print(i,end=' ')
l=15
r=25
n=r
a=[0]*(n+1)
for i in range(2,isqrt(n)+1):
    if a[i]==0:
        for j in range(i*2,n+1,i):
            a[j]=1
count=0
for i in range(l,n+1):
    if a[i]==0:
        count+=i
print(count)