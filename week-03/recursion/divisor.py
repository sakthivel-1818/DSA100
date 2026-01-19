def divisor(n,i):
    if i>n:
        return
    if n%i==0:
        print(i)
        return divisor(n,i+1)
    else:
        return divisor(n,i+1)
divisor(12,1)