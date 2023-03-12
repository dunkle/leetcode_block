# Partition Equal Subset Sum

给定一个数组，判断是否可以分成和相同的两个子集。

转换成0-1背包问题

~~~python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        # dp数组的含义是，i是否能被nums中的数相加而成
        dp = [0] * (s+1)
        dp[0] = 1
        for n in nums:
            # 从后向前遍历，如果c-n可以被组成，则c-n加上当前的数也可以被组成
            for c in range(total, n-1, -1):
                if dp[c-n]:
                    dp[c] = True
        return dp[target]
~~~

