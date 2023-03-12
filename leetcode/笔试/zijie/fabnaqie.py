#coding=utf-8
import sys
#str = input()
#print(str)
# 1 1 2 3 5 8
def fab(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 1
    return fab(n-1)+ fab(n-2)
def fab2(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
def f(n):
    def matrix_(a, k):
        a0 = a[0][0]
        a1 = a[0][1]
        a2 = a[1][0]
        a3 = a[1][1]
        if k==1:
            return a0,a1,a2,a3
        # k = 4
        if k%2==0:
            a0,a1,a2,a3 = matrix_(a, k//2)
            a0, a1, a2, a3 = a0*a0 + a1*a2, a0*a1 + a1*a3, a2*a0 + a3*a2, a2*a1 + a3*a3
            return a0,a1,a2,a3
        # k=5
        else:
            a0,a1,a2,a3 = matrix_(a, k//2)
            a0, a1, a2, a3 = a0*a0 + a1*a2, a0*a1 + a1*a3, a2*a0 + a3*a2, a2*a1 + a3*a3
            #             [[a0, a1], [a2,a3]] = [[a0*1+a1*1, a0*1+a1*1],[a2*1+a3*1, a2*1+a3*1]]
            a0, a1, a2, a3 = a0*1 + a1*1,a0*1 + a1*0,a2*1 + a3*1,a2*1 + a3*0
            return a0,a1,a2,a3

    a = [[1,1], [1,0]]
    a0,a1,a2,a3 = matrix_(a, n-1)
    return a0
    # n n-1 n-2
# n      -> 1
# n-1 n-2 -> 2
#n-2 n-3 n-3 n-4 ->4
#(1+ 2+4 + 8...+n)* n
# 2^n
# (1+
res = fab(4)
print(res)
res = fab2(15)
print(res)
res = f(15)
print(res)