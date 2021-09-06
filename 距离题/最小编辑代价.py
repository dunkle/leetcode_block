#
# min edit cost
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @param ic int整型 insert cost
# @param dc int整型 delete cost
# @param rc int整型 replace cost
# @return int整型
# https://interview.nowcoder.com/interview/27744771/interviewee?code=2yS2r8Ts
class Solution:
    def minEditCost(self , str1 , str2 , ic , dc , rc):
        # write code here
        # 插入->ic、删除-> dc 替换->rc
        # s1->s2
        m = len(str1)
        n = len(str2)
        dp = [[0 for i in range(n)] for j in range(m)]
        if str1[0]==str2[0]:
            dp[0][0] = 0
        else:
            dp[0][0] = min(rc, ic+dc)

        for i in range(1,m):
            if str1[i]==str2[0]:
                dp[i][0]= dc*(i-1)
            else:
                dp[i][0] = min(ic+i*dc, rc+(i-1)*dc)
        # s1->s2
        for i in range(1, n):
            if str1[0]==str2[i]:
                dp[0][i]= ic*(i-1)
            else:
                # s1只有一个字符，s2有i个字符，有两种选择
                # 对s1插入一个字符与s2匹配，那么 -》ic +dp[0][i-1] 转化为子问题
                # 对s1删除一个字符,那么必须得插入i个字符才能与s2匹配
                dp[0][i] = min(ic+dp[0][i-1], dc+i*ic)
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if str1[i]==str2[j]:
                    # 状态转移 两个字符以 i,j 字符结尾最少需要多少次编辑
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 将s1 转化为 s2的字符，因此需要对s1 删除那么s1字符长-1，对s1插入,s2字符长-1，替换都-1
                    dp[i][j] = min(dp[i-1][j]+dc, dp[i-1][j-1]+rc, dp[i][j-1]+ic)
        return dp[m-1][n-1]
a = Solution()
res = a.minEditCost("abc","adc",5,3,100)
print(res)
