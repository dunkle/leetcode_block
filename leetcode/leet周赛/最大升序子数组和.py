class Solution:
    def maxAscendingSum(self, nums) -> int:
        num = [3,6,10,1,8,9,9,8,9]
        n = len(nums)
        if n<1:
            return 0
        maxnum = nums[0]
        step = nums[0]
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                step+=nums[i]
                maxnum = max(maxnum, step)
            else:
                step = nums[i]
        return maxnum
a = Solution()
nums = [3,6,10,1,8,9,9,8,9]
print(a.maxAscendingSum(nums))