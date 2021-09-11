class Solution:
    def maxProfit(self, prices) -> int:
        '''
        一次遍历，从头往后，每次记录当前位置之前存在的最小股票
        到今天，股票能盈利，利用当前的price-历史最低的股票价格
        时间复杂度O(n),空间O(1)
        '''
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            # 记录最大盈利
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit
    def maxProfit_1(self, prices) -> int:
        n = len(prices)
        if n==1:
            return 0
        dp = [0 for i in range(n)]
        # 倒推记录每个位置之后能到的最高价格
        dp[n-1] = prices[n-1]
        for i in range(n-2,-1,-1):
            if prices[i]>dp[i+1]:
                dp[i] = prices[i]
            else:
                dp[i] = dp[i+1]
        # print(dp)
        # 遍历每个位置的股票价格，当前盈利为
        # 以后最高价格于当前价格之差
        res = 0
        for i in range(n):
            if dp[i]-prices[i]>res:
                res = dp[i]-prices[i]
        return res