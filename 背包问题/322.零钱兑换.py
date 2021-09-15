'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        m = len(coins)
        if m==0:
            return -1
        dp = [[float("inf") for i in range(amount+1)] for j in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(1,m+1):
            for j in range(1,amount+1):
                # i-1开始判断
                if j>=coins[i-1]:
                    dp[i][j] = min(dp[i][j-coins[i-1]] +1,dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        if dp[-1][-1]!=float("inf"):
            return dp[-1][-1]
        return -1
a = Solution()
coins = [1, 2, 5]
amount = 11
res = a.coinChange(coins, amount)
print(res)