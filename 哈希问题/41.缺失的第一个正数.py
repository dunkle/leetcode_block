'''
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1


提示：

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = len(nums)
        if m < 1:
            return 1
        count = 0
        # 统计数组有多少数字是小于0 的，多少是大于0的，将小于0的数字置为0
        # 那么正数就有 count 个数
        for i in range(m):
            if nums[i] <= 0:
                nums[i] = 2**31 - 1
            else:
                count += 1
        # 在所有的正数里，假设有 n个正数，那么只有 1-n之间的数字才有可能
        # 其他如果包含大于 n的正数，那么必定有1-n之间的数字缺失
        for i in range(m):
            # 这个位置采用的方法是 用当前位置的abs值，把对应hash位置的值置为负数
            # 很巧妙的操作，可以通过abs还原该位置的值，而不用再使用空间存储原来位置的值
            tmp = abs(nums[i])
            # abs已经默认值大于0，并且要小于 m-count(0~n-1)
            if tmp <=count:
                nums[tmp - 1] = -abs(nums[tmp - 1])
            # 当前位置的值 比count 还要大，置为0
        # print(nums)
        for i in range(m):
            if nums[i] > 0:
                return i + 1
        return count + 1



