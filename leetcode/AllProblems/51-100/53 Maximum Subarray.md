# 53 Maximum Subarray

最大的子数组和

![image-20200329130857748](../../../.assert/image-20200329130857748.png)

## 动态规划

问题是求max_sum_subarray,如果将答案设置为max_sum_subarray(array, i, j)也即[i,j]之间的最大数组，这样没办法将这个解细分成子问题，用子问题来解决这个问题。将问题转为max_sum_subarray(array, i)也即以i为右侧得数组得最大和，则状态转移方程为:
$$
C[i] =\begin{cases}
A[i] + C[i-1] ,& \text{if} A[i] + C[i-1] > A[i] \\
A[i],& \text{otherwise}
\end{cases}
$$

~~~python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = [0]*len(nums)
        max_sum[0] = nums[0]
        for i in range(1, len(nums)):
            max_sum[i] = nums[i] if nums[i] + max_sum[i-1] < nums[i] else nums[i] + max_sum[i-1]
        return max(max_sum)
~~~

## 分治法

首先将数组从中间位置分成两部分，则最大和子数组共存在于三个位置：

1. 左侧数组
2. 右侧数组
3. 以中间位置为结尾的左侧数组和以中间位置为开头的右侧数组组成的数组。

注意对于第三种情况，从中间开始向两边遍历，左右两侧的最大值设置为0，只有比0大才加到最后的结果中。

~~~

class Solution:
    import math
    def maxSubArray(self, nums: List[int]) -> int:
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 0:
                return -math.inf
            l, r = 0, len(nums)
            mid = len(nums)//2
            
            lmax = helper(nums[:mid])
            rmax = helper(nums[mid+1:])
            s, lm, lr = 0, nums[mid], 0
            for i in range(mid, -1, -1):
                s += nums[i]
                lm = max(s, lm)
            s = 0
            for i in range(mid+1, len(nums)):
                s += nums[i]
                lr = max(s, lr)
            
            if lm == -math.inf:
                lm = 0
            if lr == -math.inf:
                lr = 0
            print(lmax, rmax, lm, lr)
            return int(max(max(lmax, rmax), lm+lr))
        
        return helper(nums)
~~~

