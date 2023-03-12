#coding=utf-8
import sys
#str = input()
#print(str)

def printmatr(arr):
    m = len(arr)
    n = len(arr[0])
    if m==0:
        return []
    res = []
    l,r = 0, n-1
    t,b = 0, m-1
    while True:
        # 从左到右
        for i in range(l,r+1):
            res.append(arr[t][i])
        t+=1
        if t>b:
            break
        # 从上到下
        for i in range(t,b+1):
            res.append(arr[i][r])
        r-=1
        if l>r:
            break
        # 从右到左
        for i in range(r,l-1,-1):
            res.append(arr[b][i])
        b-=1
        if t>b:
            break
        # 从下到上
        for i in range(b,t-1,-1):
            res.append(arr[i][l])
        l+=1
        if l>r:
            break
    return res
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8,],
       [9, 10, 11, 12]]
res = printmatr(arr)
print(res)