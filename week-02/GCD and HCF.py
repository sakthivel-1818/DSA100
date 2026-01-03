
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)
gcd(a=28,b=20)




