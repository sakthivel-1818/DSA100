##selection sort
# arr=[13,46,24,52,20,9]
# n=len(arr)
# for i in range(n):
#     min_i=arr[i]
#     for j in range(i,n):
#         if arr[j]<min_i:
#             arr[i],arr[j]=arr[j],arr[i]
#
# print(arr)


##bubble sort
# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#print(arr)

###insertion sort
# for i in range(1,n):
#     key=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
#         j=j-1
#     arr[j+1]=key
# print(arr)


###////merge sort
# def merge(arr, low, mid, high):
#     temp = []
#
#     left = low
#     right = mid + 1
#
#     # Merge two sorted halves
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
#
#     # Copy remaining elements from left half
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1
#
#     # Copy remaining elements from right half
#     while right <= high:
#         temp.append(arr[right])
#         right += 1
#
#     # Copy temp back to original array
#     for i in range(low, high + 1):
#         arr[i] = temp[i - low]

# def ms(arr, low, high):
#     if low == high:
#         return
#
#     mid = (low + high) // 2
#
#     ms(arr, low, mid)
#     ms(arr, mid + 1, high)
#     merge(arr, low, mid, high)


# def mergeSort(arr, n):
#     ms(arr, 0, n - 1)


# Example usage
# arr = [8, 3, 7, 4, 2, 6]
# mergeSort(arr, len(arr))
# print(arr)

# ###example merge sort
# m=3
# nums2=[2,5,6]
# n=3
# num3=[]
# i=0
# j=0
# nums1=[1,2,3,0,0,0]
# while i < m and j < n:
#     if nums1[i] < nums2[j]:
#         num3.append(nums1[i])
#         i += 1
#     else:
#         num3.append(nums2[j])
#         j += 1
#
#
# while i < m:
#     num3.append(nums1[i])
#     i += 1
#
#         # Add remaining elements from nums2
# while j < n:
#     num3.append(nums2[j])
#     j += 1
#
#         # Modify nums1 in-place
# for i in range(m + n):
#     nums1[i] = num3[i]
#
# print(nums1)



#quick sort
# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high
#
#     while i < j:
#         # move i to the right
#         while i <= high-1 and arr[i] <= pivot:
#             i += 1
#
#         # move j to the left
#         while j >= low+1 and arr[j] > pivot:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     # place pivot in correct position
#     arr[low], arr[j] = arr[j], arr[low]
#     print(arr)
#     return j
#
#
# def qs(arr, low, high):
#     if low < high:
#         pindex = partition(arr, low, high)
#         qs(arr, low, pindex - 1)
#         qs(arr, pindex + 1, high)
#
#
# def quickSort(arr):
#     qs(arr, 0, len(arr) - 1)
#     return arr
# a=[4,6,2,1,7,9,5,3]
# print(quickSort(a))