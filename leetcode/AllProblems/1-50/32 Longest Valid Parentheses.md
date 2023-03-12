![image-20200913101618402](../../../.assert/image-20200913101618402.png)

求最长的有效括号的长度。



一开始想的是用$dp[i][j]$表示i-j之间的最长有效长度，但是当i,j可以构成一个有效的对时，$dp[i][j]=dp[i-1][j-1]+1$，这里无法判断s[i+1:j-1]之间字符串是否有效就强行加1了。

字符串动态规划的另一种思路是用一维数组：

dp[i]表示以i为结尾的最大(小)的性质，例如本题中，dp[i]表示以i结尾的最长有效括号的长度。使用一维dp，则状态只与之前的状态有关。

分析题意，括号序列是否有效主要看')'及其前一个字符，若二者组成为'()'则:
$$
dp[i] = dp[i-2] + 2
$$
若为'))'，那么假设前一个括号构成了有效的括号串，且构成的括号串长度为dp[i-1]，则与当前括号对应的括号下标为$i-dp[i-1]-1$，则有：
$$
dp[i] = dp[i-1] + dp[i-dp[i-1]-1] + 2 \quad if\quad s[i-dp[i-1]-1]='('
$$
否则为0

~~~python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    pre_valid = dp[i-2] if i > 2 else 0
                    dp[i] = pre_valid + 2
                if s[i-1] == ')':
                    if i > dp[i-1] and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + 2 
                        if i-dp[i-1] >= 2:
                            dp[i] += dp[i-dp[i-1]-2]
        if len(s) == 0:
            return 0
        return max(dp)
~~~

