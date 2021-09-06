'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
限制：

1 <= n <= 11
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
:param n:
:return:
'''
class Solution:
    def dicesProbability(self, n: int):
        # 暴力解法
        p0 = 1/6.0
        res = {}
        # 递归做法，把当前还剩多少骰子记录，并且记录当前骰子之和，到目前状态的概率
        def recur(n, number, p):
            if n==0:
                if number in res:
                    res[number] += p
                else:
                    res[number] = p
                return
            for i in range(1,7):
                recur(n-1, number+i, p*p0)
        recur(n, 0, 1)

        return [res[num] for num in res]
    def dicesProbability(self, n: int):
        # dp解法
        p0 = 1/6.0
        res = {}
        dp = [1 for i in range(n)]


        return [res[num] for num in res]
a = Solution()
n = 10
res = a.dicesProbability(n)
print(res)