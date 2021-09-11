class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        时间复杂度 O(n)空间复杂度 O(n)
        '''
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        if n<2:
            return dp[n]
        dp[2] = 2
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
    def climbStairs1(self, n: int) -> int:
        #时间复杂度 O(n)空间复杂度 O(1)
        if n==1 or n==2: return n
        a, b, temp = 1, 2, 0
        for i in range(3,n+1):
            temp = a + b
            a = b
            b = temp
        return temp
    def climbStairs2(self, n: int) -> int:
        #时间复杂度 O(1)空间复杂度 O(1)
        import math
        sqrt5=5**0.5
        fibin=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibin/sqrt5)

    def climbStairs3(self, n):
        '''
        快速幂解法
        [ 1 1 ]  [ f(n) ]    -> [ f(n) + f(n-1)] -> [ f(n+1)]
        [ 1 0 ]  [ f(n-1)]   -> [   f(n) ]       -> [  f(n) ]
        '''
        pass