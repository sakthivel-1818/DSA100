from cmath import inf

arr=[1,1,1,1]
n=len(arr)
f=arr[0]
s=float(inf)
for i in range(n):
    if f>arr[i]:
        f=arr[i]
    elif f<arr[i]<s:
        s=arr[i]
if s==float(inf):
    print(-1)
print(f,s)
