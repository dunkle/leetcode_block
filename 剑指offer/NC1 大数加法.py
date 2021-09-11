class Solution:
    def solve(self , s , t ):
        # write code here
        res = ''
        m = len(s)
        n = len(t)
        if m>n:
            s,t  = t, s
        i = len(s)-1
        j = len(t)-1
        flag = 0
        # 从后往前加
        while i>=0:
            a = s[i]
            b = t[j]
            now = int(a) + int(b) +flag
            flag = now//10
            modnum = now%10
            res = str(modnum)+ res
            i-=1
            j-=1
        # 进位继续往前
        while j>=0:
            a = int(t[j]) + flag
            flag = a//10
            modnum = a%10
            res = str(modnum) + res
            j-=1
        # 最后一位进位是否为1
        if flag:
            res = '1' + res
        return res

a = Solution()
s = "9"
t = "99999999999999999999999999999999999999999999999999999999999994"

s ="733064366"
t="459309139"
res = a.solve(s, t)
print(res)