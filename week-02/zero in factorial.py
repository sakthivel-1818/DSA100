# n=51
# fact=1
# for i in range(2,n+1):
#     fact=fact*i
# print(fact)
# count=0
# while fact>0:
#     ld=fact%10
#     if ld==0:
#         count+=1
#     elif ld!=0:
#         break
#     fact=fact//10
# print(count)

#optimize
n=15
count=0
while n>=5:
    count+=n//5 ##/ TRAILING ZERO IN FACTORIAL/
    n=n//5
print(count)

