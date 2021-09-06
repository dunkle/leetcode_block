'''
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
说明:

0 < nums.length <= 50000
0 < nums[i] < 1000
0 <= k < 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        '''
        假设现在窗口内有元素 ABC ，新来一个X后，窗口内元素为ABCX，并且仍然满足条件小于K.

        对于ABCX，新增加的子数组为X, CX, BCX, ABCX，正好等于窗口大小(rtight - left + 1).
        :param nums:
        :param k:
        :return:
        '''
        n = len(nums)
        if n < 1:
            return 0
        if k<=1:
            return 0
        ans = 1
        left = 0
        count = 0
        # 给定两个指针 i-》j
        for right in range(n):
            # 从左到右累乘
            ans *= nums[right]
            # 当累乘的结果大于K的时候，判断以right为边界的数组小于K的值有多长
            while ans >= k:
                # 去除左边界
                ans = ans / nums[left]
                left+=1
            # 在整个 left 到right 边界里可以利用上述的数组数量关系
            # 新增加的子数组为X, CX, BCX, ABCX，新增加的数组数量，正好等于窗口大小(right - left + 1)
            count += right - left + 1
        return count
