class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        暴力解法，从1开始一直往后判断，后面的丑数可以由前面的丑数 *2 *3 *5 获得
        因此对与 数字 i 判断是否可以被 2 3 5整除之后的值 在 dp里。
        :param n:
        :return:
        '''
        if n == 1:
            return 1
        flag = 1
        i = 2
        dp = [1, 2, 3, 4, 5]
        while True:
            # print(i)
            if i % 2 == 0 and i // 2 in dp:
                flag += 1
                dp.append(i)
                i += 1
            elif i % 3 == 0 and i // 3 in dp:
                flag += 1
                dp.append(i)
                i += 1
            elif i % 5 == 0 and i // 5 in dp:
                flag += 1
                dp.append(i)
                i += 1
            else:
                i += 1
            if flag == n:
                break
        return i - 1

    def nthUglyNumber_1(self, n: int) -> int:
        '''
        理解为 三个数组有序合并，设置三个指针进行往前移动
        a = [1*2 2*2 3*2 4*2 5*2 6*2]
        b = [1*3 2*3 3*3 4*3 5*3]
        c = [1*5 2*5 3*5 4*5]
        https://leetcode-cn.com/problems/chou-shu-lcof/solution/chou-shu-ii-qing-xi-de-tui-dao-si-lu-by-mrsate/
        :param n:
        :return:
        '''
        i, j, k = 0, 0, 0
        dp = [1 for i in range(n)]
        for flag in range(1, n):
            dp[flag] = min(2 * dp[i], 3 * dp[j], 5 * dp[k])
            if dp[flag]==dp[i]*2:
                i+=1
            if dp[flag]==dp[j]*3:
                j+=1
            if dp[flag]==dp[k]*5:
                k+=1
        print(dp)
        return dp[-1]
            


a = Solution()
n = 10
res = a.nthUglyNumber(n)
res2 = a.nthUglyNumber_1(n)
print(res)
print(res2)
