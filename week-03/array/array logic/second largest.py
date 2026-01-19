arr=[10,10,10]
n=len(arr)
count1=-1
for i in range(n):
    if arr[i]>count1:
        count1=arr[i]
count=-1
for i in range(n):
    if arr[i]>count and arr[i]!=count1:
        count=arr[i]
print(count)

