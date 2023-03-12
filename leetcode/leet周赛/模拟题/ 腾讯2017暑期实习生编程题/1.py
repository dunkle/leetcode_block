'''
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.



输出描述:

对于每组数据，输出一个整数，代表最少需要删除的字符个数。


输入例子1:
abcda
google

输出例子1:
2
2
'''
def delstr(s):
    t = s[::-1]
    n = len(s)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1]==s[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][n]
if __name__ == '__main__':
    s = 'abab'
    s = 'google'
    s = 'abcda'
    num = delstr(s)
    print(num)