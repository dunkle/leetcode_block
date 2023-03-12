class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if not s:
            return False
        n = len(s)
        # maxlen1 = 0
        # maxlen0 = 0
        if s[0]=='1':
            len1 = 1
            len0 = 0
        else:
            len0 = 1
            len1 = 0
        maxlen1 = len1
        maxlen0 = len0
        if n>1:
            for i in range(1, n):
                if s[i]=='1' and s[i-1]=='1':
                    len1+=1
                    maxlen1= max(maxlen1, len1)
                elif s[i]=='1' and s[i-1]=='0':
                    len1 = 1
                    maxlen1= max(maxlen1, len1)
                elif s[i]=='0' and s[i-1]=='0':
                    len0+=1
                    maxlen0= max(maxlen0, len0)
                elif s[i]=='0' and s[i-1]=='1':
                    len0 = 1
                    maxlen0= max(maxlen0, len0)
        return maxlen1>maxlen0

a = Solution()
s = '1'
s = '0'
s = "110100010"
s = "1101"
s = ''
res = a.checkZeroOnes(s)
print(res)