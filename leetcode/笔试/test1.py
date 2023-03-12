n = input()
while 1:
    num = int(input())
    arr = list(map(int, input().split()))
    lenth = len(arr)
    dp = [0 for i in range(lenth)]
    if lenth==1:
        print(lenth)
    if lenth>1:
        if arr[1]%2==0:
            dp[1]= arr[1]//2
        else:
            dp[1] =arr[1]//2+1
        if lenth==2:
            print(dp[1])
        else:
            if arr[2]%2==0:
                mid = arr[2]//2
            else:
                mid = arr[2]//2+1
            dp[2] = max(dp[1]+mid, arr[2])
            for i in range(3, lenth):
                if arr[i]%2==0:
                    zhongjian = arr[i]//2
                else:
                    zhongjian = arr[i]//2+1
                dp[i] = max(dp[i-1]+zhongjian, dp[i-2]+arr[i])
            print(dp[lenth-1])

import sys
# sys.stdin.readlines()
num = int(sys.stdin.readlines())
print(num)
# arr = list(map(int, sys.stdin().strip().split()))
# lenth = len(arr)
# dp = [0 for i in range(lenth)]
# if lenth==1:
#     print(lenth)
# if lenth>1:
#     if arr[1]%2==0:
#         dp[1]= arr[1]//2
#     else:
#         dp[1] =arr[1]//2+1
#     if lenth==2:
#         print(dp[1])
#     else:
#         if arr[2]%2==0:
#             mid = arr[2]//2
#         else:
#             mid = arr[2]//2+1
#         dp[2] = max(dp[1]+mid, arr[2])
#         for i in range(3, lenth):
#             if arr[i]%2==0:
#                 zhongjian = arr[i]//2
#             else:
#                 zhongjian = arr[i]//2+1
#             dp[i] = max(dp[i-1]+zhongjian, dp[i-2]+arr[i])
#         print(dp[lenth-1])


import sys
n = int(sys.stdin.readline().strip())
count = 1
while 1:
    if count>n:
        break
    num = int( sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    lenth = len(arr)
    dp = [0 for i in range(lenth)]
    if lenth==1:
        print(lenth)
    if lenth>1:
        if arr[1]%2==0:
            dp[1]= arr[1]//2
        else:
            dp[1] =arr[1]//2+1
        if lenth==2:
            print(dp[1])
        else:
            if arr[2]%2==0:
                mid = arr[2]//2
            else:
                mid = arr[2]//2+1
            dp[2] = max(dp[1]+mid, arr[2])
            for i in range(3, lenth):
                if arr[i]%2==0:
                    zhongjian = arr[i]//2
                else:
                    zhongjian = arr[i]//2+1
                dp[i] = max(dp[i-1]+zhongjian, dp[i-2]+arr[i])
            print(dp[lenth-1])
    count+=1