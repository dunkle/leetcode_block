class Solution:
    def lengthOfLIS(self, nums) -> int:
        '''
        dp[i] 代表 对于以第nums[i]为结尾，之前的最长子序列
        以i为结尾往前j遍历，如果 nums[i] > nums[j]
        则在以 j字符结尾的最长子序列基础上再+1
        dp[i] = dp[j]+1 其中j 从0->i 遍历

        '''
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
                    # print(dp)
        return max(dp)