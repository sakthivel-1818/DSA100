arr = [1, 2, 3, 2, 1]
rev=[]
for i in range(len(arr),0,-1):
    rev.append(arr[i-1])
if rev==arr:
    print(True)
else:
    print(False)