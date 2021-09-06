class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        def robmoney(nums):
            m = len(nums)
            dp = [0]*m
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, m):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[m-1]
        # 偷第一个：
        firstrob = robmoney(nums[:n-1])
        # 偷最后一个
        lastrob = robmoney(nums[1:])
        return max(firstrob, lastrob)

a = Solution()
nums = [2,3,2]
nums = [1,2,3,1]
res = a.rob(nums)
print(res)