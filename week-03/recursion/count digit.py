def printNos(n):
    if n == 0:
        return 0
    return n + printNos(n-1)
print(printNos(3))