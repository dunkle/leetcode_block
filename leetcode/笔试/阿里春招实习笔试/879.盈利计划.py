'''
集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 minProfit 利润的子集称为盈利计划。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

 

示例 1：

输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。
示例 2：

输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
 

提示：

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/profitable-schemes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:
        '''
        三个状态
        物品总数 也就是 group 和 profit 的数组长度
        对第i个物品有两种状态，选 或者不选
        第一个状态 也就是 所有人数 最多取一次，相当于 背包容量

        -》当选择时 需要 消耗 group i 个人 也就是 占据的背包体积
                  同时获得价值 profit i的价值
        第二个状态 也就是 价值总量 profit ，需要选出价值总量 大于 minprofit 的 物件数
        因此
        对 第i 件物品 需要做出如下判断

        当需要耗费的体积大小大于 剩余背包容量时，则不选，当前状态 仍然时上一物品状态
        当小于 剩余背包容量， 需要判别 所选取的物品价值，与 还需要补充的价值 之差，如果 所选大于剩余补充，说明需要选取该物品，价值总和满足
        :param n:
        :param minProfit:
        :param group:
        :param profit:
        :return:
        '''
        m = len(group)
        mod = 10**9+7
        dp =[ [[0 for i in range(minProfit+1)] for j in range(n+1)] for k in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                dp[i][j][0] = 1
        for k in range(1, m+1):
            for i in range(1, n+1):
                for j in range(minProfit, -1, -1):
                    dp[k][i][j] = dp[k-1][i][j]
                    if i>=group[k-1]:
                        dp[k][i][j] = dp[k-1][i-group[k-1]][max(0, j-profit[k-1])] + dp[k-1][i][j]
                    dp[i][j][k] = dp[i][j][k] % mod
        print(dp[m][n][minProfit])
        return dp[m][n][minProfit]

a = Solution()
n = 5
minProfit = 3
group = [2,2]
profit = [2,3]
a.profitableSchemes(n, minProfit, group, profit)