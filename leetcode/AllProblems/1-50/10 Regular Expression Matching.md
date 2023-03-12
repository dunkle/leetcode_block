# Regular Expression Matching

![image-20200830211015818](../../../.assert/image-20200830211015818.png)

实现正则表达式中的'.'和'*'匹配。

## 递归实现

给定一个字符串和一个正则表达式，如果正则表达式中仅包含'.'，那么只需要判断每个字符串的开头是否相同或正则表达式为'.'即可。

~~~python
def isMatch(s, p):
    if not p:
        return not s
    
    first_match = bool(s) and p[0] in {s[0], '.'}
    return first_match and isMatch(s[1:], p[1:])
~~~

如果加入了'\*'这种匹配，那么还需要判断当前字符的下一个字符是否为'\*'

~~~python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
~~~



## 动态规划实现

用dp[i,j]表示s[:i]与p[:j]是否匹配。则算法为：

~~~python
def isMatch(s, p):
   	dp = [[False]*(len(p)+1) for _ in range(len(s) + 1)]
    # 二者都为空串的情况为True
    dp[-1][-1] = True
    
    # i 从空字符串(最后一个位置)开始，判断p能否匹配
    for i in range(len(s), -1, -1):
        # 匹配串从最后一个字符匹配开始
        for j in range(len(p)-1, -1, -1):
            # 首先判断匹配串和正则表达式第一个字母是否相同
            first_match = i < len(s) and p[j] in {s[i], '.'}
            # 然后判断当前正则表达式的下一个字符是否为'*’
            if j+1 < len(p) and p[j+1] == '*':
                # or之前的部分是使用‘*’匹配空字符串，or之后的部分是使用‘*’匹配一次当前字符
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                # 如果不为‘*’，那就仅进行当前字符的匹配
                dp[i][j] = first_match and dp[i+1][j+1]
~~~

