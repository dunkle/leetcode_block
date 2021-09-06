'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0

示例 4：
输入：s = ")(())"
输出：4
解释：最长有效括号子串是 "(())"


提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        有效字符串有两种情况
        1、以 s[i] “）” 结尾, 恰好与前一个 s[i-1] "（" 匹配 dp[i] = dp[i-2] +2
        2、以 s[i] “）” 结尾， 前一个字符也是 “）”，此时需要判断
            如果连续的两个“）” 都能成有效字符串的时候需要满足
            dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                最外侧的 第i个位置，“）”  与 i-dp[i-1] -1 的位置匹配 "（"
                dp[i] 代表的是有效字符的长度。
                下标 0 1 2 3 4 5 6 7 8 9
                字符 ( ) ( ( ( ( ) ) ) )
                情况     j |- dp[i-1]-| i
                数值 0 2 0 0 0 0 2 4 6
       这个2(下标1) 就是dp[i - dp[i - 1] - 2] = dp[9 - dp[9 - 1] -2] = dp[9 - 6 - 2] = dp[1]

        :param s:
        :return:
        '''
        n = len(s)
        maxlen = 0
        dp = [0 for i in range(n)]
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    # 相邻两个括号匹配成功 +2 字符长度
                    dp[i] = dp[i-2] +2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    if i-dp[i-1]-1>0:
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = dp[i-1] +2
                # print(dp)
                maxlen = max(maxlen, dp[i])
        return maxlen

a = Solution()
s = ")(())"
s = ""
s = ")()())"
res = a.longestValidParentheses(s)
print(res)