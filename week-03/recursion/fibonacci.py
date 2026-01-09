
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(6))

n=5
if n==0:
    print(0)
if n==1:
    print(1)
a,b=0,1
for i in range(2,n+1):
    a,b=b,a+b
print(a)