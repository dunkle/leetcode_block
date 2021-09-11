'''
239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
示例 4：

输入：nums = [9,11], k = 2
输出：[11]
示例 5：

输入：nums = [4,-2], k = 2
输出：[4]

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        import collections
        res = []
        queue = collections.deque()
        # 建立一个双端队列，用来存储位置坐标，从左往右值是递减的
        for i, num in enumerate(nums):
            # 保持窗口的大小是k
            if queue and queue[0] == i - k:
                queue.popleft()

            # 到当前位置了，有最大值，就需要剔除所有比较小的值
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                # 每次把最大的放入结果就行，最大的是队列最左侧的值
                res.append(nums[queue[0]])
        return res
    def maxSlidingWindow2(self, nums, k):
        res = []
        # queue 值应该是一个递减的序列，第一个元素为最大值。
        queue = []
        for i in range(len(nums)):
            # 保持当前窗口的列表长度为k,因此当 下标i 减去队列第一个元素（最大值下标）==k
            # 此时队列长度已经超出k
            if queue and i-queue[0]==k:
                # 剔除队列的第一个元素
                queue.pop(0)
            # 达到当前下标i时，判断当前窗口内，比当前值小的元素，全部剔除。
            # 假设 queue下标指引的值对应 4 2 1  当前值为3，因此剔除2，1因为窗口始终保持，3最大
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            # 把当前下表加入队列，表示达到当前窗口最远距离
            queue.append(i)
            # 从起始位置开始，只有序列长度大于k时，才开始窗口滑动
            if i>=k-1:
                # 每次滑动一个位置都需要 把结果记录
                res.append(nums[queue[0]])
        return res


a = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = a.maxSlidingWindow(nums, k)
res = a.maxSlidingWindow2(nums, k)
print(res)