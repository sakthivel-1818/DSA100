n=325345
temp=0
while n>0:
    ld=n%10
    n=n//10
    temp = temp*10 +ld
print(temp)