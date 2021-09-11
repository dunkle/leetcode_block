import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if k>n:
            return [max(nums)]
        queue = [0]
        res =[]
        for i in range(1,k):
            while nums[i]>nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        for i in range(k,n):
            if i-queue[0]<k:
                res.append(queue[0])
            while nums[i]>nums[queue[-1]]:
                queue.pop()
            queue.append(i)

a = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = a.maxSlidingWindow(nums, k)
print(res)