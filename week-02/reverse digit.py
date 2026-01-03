n=12305
rev=0
while n>0:
    ld=n%10
    if ld==0:
        n=n//10
    else:
        n = n // 10
        rev = rev * 10 + ld
print(rev)




