# pattern-1
# for i in range(1,6):
#     for j in range(1,i):
#         print(j,end="")
#     print()

# patter-2
# for row in range(n+1):
#     for col in range(n+1):
#         print("*",end="")
#     print()

#patten-3
# for row in range(n):
#     for j in range(1,n+1):
#         print(j,end="")
#     print()

#patter-4
# for i in range(1,n+1):
#     for j in range(1):
#         print(i*"*",end=" ")
          #or
# n=3
# for i in range (1,n+1):
#     print(i*"*","",end="")
n=4
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end="")
    print()