arr= [12, 3, 15, 7, 9]
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if min>arr[i]:
        min=arr[i]
    if max<arr[i]:
        max = arr[i]

print(min,max)
