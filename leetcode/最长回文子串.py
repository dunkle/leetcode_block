def longestPalindrome(s):
    #至少要判断所有子串字符一遍，所以，至少为O(n*2)
    if not s: return ''
    n = len(s)
    if n < 2:
        return s
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    a = 0
    max_len =0
    res = s[0]
    #判断字符从0—》到j的子串是否为回文子串
    for j in range(1, n):
        for i in range(j):
            if s[i]==s[j]:
                if j-i<3: # aba i=0, j=2 and s[i]==s[j] 只剩下一个字符了，必定为回文串
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False
            if dp[i][j] ==True:
                if j-i+1 > max_len:
                    max_len = j-i+1
                    res = s[i:i+max_len]
    return res

print(longestPalindrome('abbbbac'))

