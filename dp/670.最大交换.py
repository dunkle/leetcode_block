'''
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 108]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-swap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        dp = [0 for i in range(n)]
        dp[n-1] = n-1
        for i in range(n-2, -1, -1):
            # print(i)
            if num[i]>num[dp[i+1]]:
                dp[i] = i
            else:
                dp[i] = dp[i+1]
        # print(dp)
        for i in range(n):
            if num[i]==num[dp[i]]:
                continue
            else:
                num[i], num[dp[i]] = num[dp[i]], num[i]
                break
        return int("".join(num))
a = Solution()
num = 9973

res = a.maximumSwap(num)
print(res)