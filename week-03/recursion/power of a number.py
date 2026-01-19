def powe(a,b,i):
    if i==b:
        return a
    return a * powe(a,b,i+1)
print(powe(2,3,1))