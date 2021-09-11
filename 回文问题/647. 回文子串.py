'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        以i为起点，j 字符结尾的子串是否是字符串，状态转移
        abbcbba,判断首尾字符是否相等，如果相等，则判断包含其中的子串是否是回文串
        当首尾字符串相等时，如果长度小于2 j-i<2,说明只有一个或者两个字符串。必定为回文串。
        dp[i][j] =  dp[i+1][j-1]
        时间复杂度 -> O（n^2）
        :param s:
        :return:
        '''
        n = len(s)
        if not n:
            return 0
        res = 0
        dp = [[False for i in range(n)] for j in range(n)]
        for j in range(n):
            for i in range(j+1):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res+=1
                else:
                    dp[i][j] = False
        return res