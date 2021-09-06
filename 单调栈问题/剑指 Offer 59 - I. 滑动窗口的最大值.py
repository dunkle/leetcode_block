'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：
你可以假设 k 总是有效的，在输

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口,数组初始位置到正好形成长度为k的窗口
        for i in range(k):
            # 如果队列不为空 并且队列最后一个元素是 小于新遍历的元素，保持队列 递减 不增的状态
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        # 队列初始最前端为 最大值。
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            # 窗口往右滑动，需要删除原窗口最左边的元素，添加新元素到最右侧
            # 同时要维护 递减队列， 如果删除的元素是递减队列中最大的值，则队列对应元素也需要出队列
            if deque[0] == nums[i - k]:
                deque.popleft()
            #
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res
