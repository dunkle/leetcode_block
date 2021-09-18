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
    # 上述解法是O(n^2)的时间复杂度
    def lengthOfLIS_1(self, nums) -> int:
        '''
        以i为结尾往前j遍历，如果 nums[i] > nums[j]，则在以 j字符结尾的最长子序列基础上再+1
        dp[i] = dp[j]+1 其中j 从0->i 遍历，本质上是需要不断的遍历i以前的值，直到找到比当前值小的数
        在查找的时候，可以提高算法的效率，设置一个新的记录方式，使得数组保证O(lgn)的复杂度，二分查找
        '''
        # tails 的index位置 记录的是长度为index的最长序列的尾序列值
        # 通过不断更新最小的尾序列值，二分查找的方式进行查找
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res

a = Solution()
nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]

res = a.lengthOfLIS_1(nums)
print(res)
print(a.lengthOfLIS(nums))