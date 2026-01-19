###//// reverse an array
# def func(a,l,r):
#     if l>=r:
#         return
#     a[l],a[r]=a[r],a[l]
#     return func(a,l+1,r-1)
# def main():
#     arr=[1,3,7,1,8,3,8]
#     n=len(arr)
#     func(arr,0,n-1)
#     print(arr)
# main()
#
# def func(a,i,j):
#     if i>=j/2:
#         return
#     a[i],a[j]=a[j],a[i]
#     func(a,i+1,j-i-1)
# def main():
#     arr=[1,3,7,1,8,3,8]
#     n=len(arr)
#     func(arr,0,n-1)
#     print(arr)
# main()

# same reverse a arr
# def func(a):
#     n=len(a)
#     for i in range(n//2):
#         a[i],a[n-i-1]=a[n-i-1],a[i]
# def main():
#     arr=[1,3,7,1,8,3]
#     func(arr)
#     print(arr)
# main()

# ###palindrome
# def func(i,name):
#     n=len(name)
#     if i>=n//2:
#         return True
#     if name[i] !=name[n-i-1]:
#         return False
#     return func(i+1,name)
# a="Madam"
# print(func(0,a))


