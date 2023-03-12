# 122. Best Time to Buy and Sell Stock II

![Profit Graph](../.assert/122_maxprofit_1.PNG)

一开始想的是以当前作为最低点，在之后找到一个**最高点**计算，如上图的2和5所示。此时的profit为C，但是这却不是最优的，因为中间还有一对波峰波谷，其profit和为A+B，而C<A+B,所以不是最优的贪心策略。

正确的贪心策略是，找到一个波谷，然后找到距离**最近的**波峰，得到差之后加到结果中。也即贪的不是利益最大，而是距离最短。

~~~python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while i < len(prices) - 1:
            valley = 0
            peak = 0
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            profit += peak - valley
            i += 1
        return profit
~~~

还可以继续优化的点在于，对于一段连续的上升，可直接计算波段之间的差，而不用找波峰，如下图所示：

D=A+B+C

![Profit Graph](../.assert/122_maxprofit_2.PNG)

~~~python
class Solution:
    def maxProfit(self, prices) -> int:
        result, i = 0, 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]
            i += 1
            
        return result
~~~

