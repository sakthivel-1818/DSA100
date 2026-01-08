def printNos(n):
    if n == 0:
        return 1

    printNos(n - 1)
    print(n)
printNos(10)
