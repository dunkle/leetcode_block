'''
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
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
        空间复杂度 -> O（n^2）
        :param s:
        :return:
        '''
        n = len(s)
        if n<=1:
            return s
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        maxlen = 0
        res = s[0]
        for j in range(n):
            # 以j字符结尾的字符
            for i in range(j):
                # 以i起点 j结尾字符
                # aba 如果首尾字符相同，
                # 如果只有两个ij字符 那么dp[i[[j] True / 状态转移 dp[i+1][j-1]是否为True 子串字符是否为回文
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                # print(dp)
                if dp[i][j]:
                    # 如果当前字符是回文字符，那么判断是否是最长的回文字符
                    if j-i+1>maxlen:
                        maxlen = j-i+1
                        res = s[i:j+1]
        return res

    def substring(self, s):
        '''
        中心扩散方法 依次遍历字串，对于奇数串以每一个字符作为字符中心向两端扩散。
        对于偶数串，可能存在 abba 的情况，以中心两个字符作为回文中心往外扩展
        时间复杂度 -> O（n^2）
        空间复杂度 -> O（1）
        '''
        n = len(s)
        if n==0:
            return 0
        if n==1:
            return 1
        # if n==2:
        #     return s[0]==s[1] if 2 else 1
        def ispala(i, j):
            lenth = 0
            while i>=0 and j<n:
                if s[i]==s[j]:
                    lenth = j-i+1
                    i-=1
                    j+=1
                else:
                    break
            return s[i+1:j]
        lenth = 0
        for k in range(0, n-1):
            res = ispala(k ,k)
            if len(res)>lenth:
                lenth = len(res)
                result = res
            if s[k]==s[k+1]:
                res = ispala(k ,k+1)
                if len(res)>lenth:
                    result = res
                    lenth = len(res)
        return result


a =  Solution()
s = "babad"
# s = "cbbd"
print(s)
res = a.countSubstrings(s)
print(res)
res2 = a.substring(s)
print("res2", res2)