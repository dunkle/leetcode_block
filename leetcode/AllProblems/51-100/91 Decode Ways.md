![image-20201008162822383](../../../.assert/image-20201008162822383.png)

将字母映射为数字，给定一段数字的组合，求有多少种解释方式。

类似跳格子问题，但是需要注意，如果某一位为‘0’则该位必须与上一位进行组合。

~~~python
class Solution:
    def numDecodings(self, s): 
        if not s:
            return 0
		# 这里dp数组表示的是第i位之前所能解释的数量
        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1)

        for i in range(2, len(s) + 1): 
            # 判断当前数字，排除0
            if 0 < int(s[i-1:i]) <= 9:    #(2)
                dp[i] += dp[i - 1]
            # 和前一个数字组合，可以直接从10开始判断，防止前一个为0
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
        return dp[len(s)]
            
~~~

