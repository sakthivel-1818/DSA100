####/////// print n time name
# def func(i,n):
#     if i>n:
#         return
#     print('sakthi')
#     return func(i+1,n)
# def main():
#     func(1,5)
# main()


####//// print linearly from 1 to n
# def func(i,n):
#     if i>n:
#         return
#     print(i,end="")
#     return func(i+1,n)
# def main():
#     func(1,4)
# main()
#

###///print n to 1 reverse
# def func(i,n):
#     if i<1:
#         return
#     print(i,end="")
#     func(i-1,n)
#
#
# def main():
#     func(4,4)
# main()
#
##//// backtracking n to 1
# def func(i,n):
#     if i>n:
#         return
#     func(i+1,n)
#     print(i, end="")
# def main():
#     func(1,4)
# main()

###/// back tracking 1 to n
# def func(i,n):
#     if i<1:
#         return
#     func(i-1,n)
#     print(i, end="")
# def main():
#     func(4,4)
# main()



class Solution:
    def printNos(self,n):
        if n<1:
            return 1
        return n * self.printNos(n-1)

obj=Solution()
print(obj.printNos(4))