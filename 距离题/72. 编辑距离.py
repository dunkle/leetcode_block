'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n):
            dp[i][0] = i
        for j in range(m):
            dp[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[j-1]==word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 由word2 删除一个字符得到只有word -1，但是仍然没有匹配， 由替换一个得到匹配，两者字符都-1. 由插入得到，只有word1 字符-1
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j-1]+1, dp[i-1][j]+1)
        return dp[n][m]
a = Solution()
word1 = "horse"
word2 = "ros"
num = a.minDistance(word1, word2)
print(num)