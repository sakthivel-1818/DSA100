##numbersssss how many number count in array
# arr=[1,2,5,2,1]
# n=len(arr)
# hash_arr=[0]*12
#
# for i in arr:
#     hash_arr[i]+=1
#
# queries=[2,1,4,5,3,6]
#
# for x in queries:
#     print(f"{x}={hash_arr[x]}")

##characterhash    ASSCIII CHARACTER IS 256
# a="ssaakktthhii"
#
# hash_arr=[0]*256
#
# for i in a:
#     hash_arr[ord(i)]+=1
#
# q="sakthivel"
#
# for j in q:
#     print(f"{j }={hash_arr[ord(j)]}")



arr=list(map(int,input().strip()))
n=len(arr)
hash_map={}
for i in range(n):
    if arr[i] in hash_map:
        hash_map[arr[i]]+=1
    else:
        hash_map[arr[i]]=1
q=[1,5,6,2,7]
for i in q:
    if i in hash_map:
        print(f"{i}={hash_map[i]}")
    else:
        print(f"{i}={0}")
