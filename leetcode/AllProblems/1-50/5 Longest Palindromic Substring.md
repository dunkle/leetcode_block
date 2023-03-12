# 5. Longest Palindromic Substring

![image-20200414215704301](../../../.assert/image-20200414215704301.png)

给定一个字符串，求最长的回文子串

## 动态规划

给定"ababa"，如果已知"bab"是回文串，且两侧字母相等， 则可以不用计算中间的部分。

定义$p(i,j)$为：
$$
p(i,j) = \begin{cases}
true, if s[i..j] is Palindromic \\
false, otherwise
\end{cases}
$$
则:

p(i,j) = (p[i+1, j-1] and s[i] == s[j]

初始条件为:
$$
p(i, i) = True \\
p(i, i+1) = (s[i] == s[i+1])
$$

~~~python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        dp = [[False]*len(s) for _ in range(len(s))]
        
        l = len(s)
        max_len = 1
        start = 0
        for i in range(l):
            dp[i][i] = True
        # j用来控制字符串的尾部，判断s[0:j]之间的最长回文串
        for j in range(1, l):
            # i用于控制字符串的起始位置，判断s[i:j]是否为回文串
            for i in range(j):
                if s[i] == s[j]:
                    # 在这里判断连续的两个是否相同
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i + 1 > max_len:
                    start, max_len = i, j-i+1
        return s[start:start+max_len]
~~~

时间复杂度为$O(N^2)$,空间复杂度为$O(N^2)$

## 从中间扩张

每个回文串都是以中间为中心向两边扩张的，因此可以检查2n-1个中心（奇数串和偶数串）两边是否为回文，然后记录最长的即可。

~~~python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max = ""
        for i in range(len(s)):
            s1, e1, l1 = self.expand_str(s, i, i)
            s2, e2, l2 = self.expand_str(s, i, i+1)
            start, e, l = (s1, e1, l1) if l1 > l2 else (s2, e2, l2)
            
            if len(self.max) < l:
                self.max = s[start:e+1]
        return self.max    
            
    def expand_str(self, s, i, j):
        left = i
        right = j
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (i+1, j-1, j-i-1)
~~~

每扩张一次的时间复杂度为$O(N)$,因此时间复杂度为$O(N^2)$,空间复杂度为$O(1)$



