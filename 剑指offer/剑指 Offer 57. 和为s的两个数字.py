class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        i,j = 0, n-1
        while i<j:
            if nums[i]+nums[j]<target:
                i+=1
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                return [nums[i], nums[j]]