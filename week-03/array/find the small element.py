from cmath import inf

arr=[2,5,3,5,6,0]
n=len(arr)
f=float("inf")
s=float("inf")
for i in range(n):
    if f>arr[i]:
        s=f
        f=arr[i]

    elif f<arr[i]<s:
        s=arr[i]
if s==float(inf):
    print(-1)
else:
    print(f,s)

### another method
# def smallest(self, a, n, exclude):
#          res = float('inf')
#          for i in range(n):
#              if a[i] < res and a[i] != exclude:
#                  res = a[i]
#          return res
#
#     def minAnd2ndMin(self, arr):
#          n = len(arr)
#          min1 = self.smallest(arr, n, float('inf'))
#          min2 = self.smallest(arr, n, min1)
#          if min1 == float('inf') or min2 == float('inf'):
#              return [-1]
#          return [min1, min2]
