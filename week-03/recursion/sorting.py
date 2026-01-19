
arr=[1,2,3,4,5,6,7,8,9,10,11,14,16]
n=len(arr)
# for i in range(0,n-1):
#     for j in range(0,n-1-i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)
###//// insertion sort
# for i in range(1,n):
#     key=arr[i]
#     j=i-1
#     while key<arr[j] and j>=0:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key
# print(arr)

# low=0
# high=n-1
# x=8
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==x:
#         print(mid)
#         break
#     elif arr[mid]<x:
#         low=mid+1
#     else:
#         high=mid-1
arr = [1, 3, 5, 8, 10, 12]
x = 8

low = 0
high = len(arr) - 1

# while low <= high:
#     mid = (low + high) // 2
#
#     if arr[mid] == x:
#         print(mid)
#         break
#     elif arr[mid] < x:
#         low = mid + 1
#     else:
#         high = mid - 1
