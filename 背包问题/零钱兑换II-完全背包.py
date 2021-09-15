'''
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1
 
注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def change(self, amount: int, coins) -> int:
        m = len(coins)
        dp = [[0 for i in range(amount+1)] for j in range(m+1)]
        for i in range(amount+1):
            dp[0][i] = 0
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, amount+1):
                if j-coins[i-1]>=0:
                    # 此处 dp[i][j- coins[i-1]] 易错成dp[i][j- coins[i-1]]
                    # 代表选择第i种货币 应该是 dp[i] 不选则是 dp[i-1]

                    dp[i][j] = dp[i-1][j] + dp[i][j- coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp[m][amount], dp[-1][-1])
        return dp[m][amount]

    #状态压缩
    def change_dp(self, amount: int, coins) -> int:
        m = len(coins)
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for i in range(1, m+1):
            for j in range(0, amount+1):
                if j-coins[i-1]>=0:
                    # 此处 dp[i][j- coins[i-1]] 易错成dp[i][j- coins[i-1]]
                    # 代表选择第i种货币 应该是 dp[i] 不选则是 dp[i-1]
                    dp[j] = dp[j] + dp[j- coins[i-1]]
        print(dp[amount], dp[-1])
        return dp[amount]
'''
1
'''

a = Solution()
amount =5
coins = [1, 2, 5]
# a.change(amount, coins)
a.change_dp(amount, coins)