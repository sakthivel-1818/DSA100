def printNos(n):
    if n%10==n:
        return 1
    return 1+printNos(n//10)
print(printNos(n=342))