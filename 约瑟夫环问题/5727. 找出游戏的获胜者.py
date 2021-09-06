class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = list(range(n))
        # print(res)
        idx = 0
        #此处很巧妙的只用运行n-1次即可剔除n中的n-1个数
        for i in range(n-1):
            #采用循环数组时，可以采用求模的方式进行
            idx = (idx+k-1)%len(res)
            # print(res[idx]+1)
            res.remove(res[idx])
            # print(res)
        return res[0]+1
    def findyuesefu(self, n, k):
        x = 0
        for i in range(2, n+1):
            x = (x+k)%i
        return x+1

n = 5
k = 2
a = Solution()
res = a.findTheWinner(n, k)
res2 = a.findyuesefu(n, k)
print(res, res2)
