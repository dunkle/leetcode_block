class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        '''
        3^0 = 1 3^1 = 3 3^2 = 9 3^3 = 27
        3^4 = 81 3^5 = 243
        '''
        count = 0
        arr = [0]
        while n - 3**count>=0:
            arr.append(3**count)
            count+=1
        count = len(arr)
        print(arr, n, count)
        dp = [[False for i in range(n+1)] for j in range(count+1)]
        for i in range(count+1):
            dp[i][0] = True
        for i in range(1, count+1):
            for j in range(1, n+1):
                if j-arr[i-1]>=0:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[count][n]
    def checkPowersOfThree_1(self, n: int) -> bool:
        count = 0
        arr = [0]
        while n - 3**count>=0:
            arr.append(3**count)
            count+=1
        count = len(arr)
        print(arr, n, count)
        self.flag = False
        def recur(index, num):
            if index==count:
                if num==n:
                    self.flag = True
                return
            recur(index+1, num+arr[index])
            recur(index+1, num)
        recur(0, 0)
        print(self.flag)

a = Solution()
# n = 12
n = 21
# n = 882567
# result = a.checkPowersOfThree(n)
result = a.checkPowersOfThree_1(n)
print(result)