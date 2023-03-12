# 198. House Robber

![image-20200331014823430](../../.assert/image-20200331014823430.png)

给定一维数组，只能拿不相邻的两个元素，求和最大。

**动态规划**

首先确定递归关系，也即状态转移关系：

对于当前的每一个值，只有两种选择：

1. 拿当前值和前两个的最大值
2. 不拿当前值拿前面那个的最大值

则状态转移方程为：
$$
C[i] = \text{max}(C[i-1], C[i-2] + \text{current})
$$

~~~python
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        tmp = []
        tmp.append(nums[0])
        tmp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            tmp.append(max(tmp[i-1], tmp[i-2] + nums[i]))
        return max(tmp)
~~~

