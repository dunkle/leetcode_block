# 121. Best Time to Buy and Sell Stock

找到利润最大的两个时间。用一个值保存当前遇到过的最小的波谷，判断当前的值与这个波谷的插值 是否最大。

~~~python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy = prices[0]
        result = 0
        for n in prices:
            if buy > n:
                buy = n
            elif n-buy > result:
                result = n-buy
        return result
~~~

