
arr=[1,2,3,4,5,6,90]
count=0
for i in range(len(arr)):
    if arr[i]>count:
        count=arr[i]
print(count)