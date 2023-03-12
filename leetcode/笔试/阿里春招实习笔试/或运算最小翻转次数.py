class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        pred = '{0:b}'.format(a|b)
        a = '{0:b}'.format(a)
        b = '{0:b}'.format(b)
        c = '{0:b}'.format(c)
        n = max(len(c), len(pred))

        a = '0'*(n-len(a))+a
        b = '0'*(n-len(b))+b

        pred = '0'*(n-len(pred))+pred
        c = '0'*(n-len(c))+c
        count = 0
        for i in range(n):
            if pred[i]==c[i]:
                continue
            elif pred[i]!=c[i] and c[i]=='1':
                count+=1
            elif pred[i]!=c[i] and c[i]=='0':
                if a[i]=='1':
                    count+=1
                if b[i]=='1':
                    count+=1
        return count