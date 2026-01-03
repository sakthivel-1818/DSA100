from math import isqrt
# n=5
# count=1
# i=0
# j=0
# while n!=0:
#     i+=count
#     count+=1
#     j+=i
#     n=n-1
#
# print(j)

 ### optimize
# n=5
# i=n*(n+1)//2
# print(i)
####/////1,3,6,10,15,21

###/////1+(1+2)+(1+2+3)+(1+2+3+4)
# n=5
# i=n*(n+1)*(n+2)//6
# print(i)

###1+(1+3)+(1+3+5)+(1+3+5+7)
# n=2
# i=n*(n+1)*(2*n+1)//6
# print(i)

####1^3 + 2^3 + 3^3 +4^3 + 5^3 = 225
# n=5
# j=0
# while n>0:
#     j+=n*n*n
#     n=n-1
# print(j)

# n=5
# i=(n*(n+1)//2)**2
# print(i)

####///1^5+2^5+3^5+4^5
# n=5
# i=n**2*(n+1)**2 * (2*n**2+2*n-1)//12

# n=3
####(1^2+2^2+3^2)-(1+2+3)^2
n=3
sum_n=n*(n+1)//2
sum_sq=n*(n+1)*(2*n+1)//6
total=abs(sum_sq-(sum_n)**2)
print(total)