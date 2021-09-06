'''
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
'''
def maxSubArray(nums) -> int:
    maxnum = nums[0]
    n = len(nums)
    if n<2:
        return maxnum
    res = nums[0]
    for i in range(1, n):
        # 一直连续加和，如果加和一直大于0说明对后续数据是正向的
        if res>0:
            # 当前res的值代表是到当前 位置值 之前的累加值，如果res小于0代表的是到该节点之前都是负向的
            # 因此从当前位置开始继续进行计算。
            res+=nums[i]
        # 如果加和为负，说明对后续为负向，不如从当前位置开始再加和
        # 需要声明一下，这里不使用i指针，从子数据开始位置往后移动的原因是，移动位置不如从当前位置开始
        else:
            res = nums[i]
        maxnum = max(maxnum, res)
    return maxnum

nums =[-2,1,-3,4,-1,2,1,-5,4]
res = maxSubArray(nums)
print(res)