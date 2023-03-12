# 300. Longest Increasing Subsequence

![image-20200426155340098](../../../.assert/image-20200426155340098.png)

给定一个数组，求其中的最长连续递增子序列。

动态规划，dp中每个值为该值的最长序列，则
$$
dp[i] = max(dp[j]) + 1,\quad0<j<i,\quad \text{nums}[j] < \text{nums}[i]
$$

~~~python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        result = 0
        l = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    l[i] = max(l[i], l[j]+1)
            result = max(l[i], result)
        print(l)
        return result
~~~

时间复杂度为$O(N^2)$

## 动态规划与二分查找

构造一个dp数组，数组中为当前最长的递增子序列。每遇到一个值，就找该值在子序列中的位置，然后插入该值。

![image-20200426155735060](../../../.assert/image-20200426155735060.png)