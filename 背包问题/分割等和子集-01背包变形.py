'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def canPartition(self, nums) -> bool:
        numall =0
        for i in nums:
            numall+=i
        if numall%2==1:
            return False
        numall = numall//2
        n = len(nums)
        dp = [[False for i in range(numall+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1, numall+1):
                if j-nums[i-1]>=0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] | dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp[n][numall])
        return dp[n][numall]
    def canPartition_yasuo(self, nums) -> bool:
        numall =0
        for i in nums:
            numall+=i
        if numall%2==1:
            return False
        numall = numall//2
        n = len(nums)
        dp = [False for i in range(numall+1)]
        dp[0] = True
        for i in range(1,n+1):
            for j in range(numall, 0, -1):
                if j-nums[i-1]>=0:
                    dp[j] = dp[j-nums[i-1]] | dp[j]
        print(dp[numall])
        return dp[numall]
a = Solution()
nums = [1, 5, 11, 5]
# a.canPartition(nums)
a.canPartition_yasuo(nums)