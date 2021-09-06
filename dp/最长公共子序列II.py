#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1 , s2 ):
        # write code here
        m = len(s1)
        n = len(s2)
        # m 行 n 列
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i,j=m,n
        res = ''
        # 需要倒序查找到对应的字符，进行遍历
        while i>0 and j>0:
            # 倒序找，字符相等直接添加到最后结果
            if s1[i-1]==s2[j-1]:
                res = s1[i-1]+res
                i-=1
                j-=1
            else:
                # 不相等，需要判断删减哪个值
                if dp[i-1][j]>dp[i][j-1]:
                    i-=1
                else:
                    j-=1
        if len(res)==0:
            return -1
        return res