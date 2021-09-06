'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    # 方法一
    def subarraySum(self, nums, k: int) -> int:
        dic = {}
        acc, res = 0, 0
        for num in nums:
            acc += num
            if acc == k: res += 1
            # 此处使用acc-k 比较精妙，假设加到此时 acc 的值为 i， 通过 acc -k的值，找到在dict中的位置假设为j，说明从开始加到j的值为acc-k
            # 说明 i到j位置正好为k
            if acc - k in dic: res += dic[acc - k]
            # 给dict acc 出现的次数计数，如果没有计数为0
            dic[acc] = dic.get(acc, 0) + 1
        return res
    # 方法二
    def subarrray(self, nums, k):
        # 这种做法就是常规的前缀和的思路，先求达到位置i的累积和，
        # 然后用两个指针 i，j 分别移动，dp[j]-dp[i] 即为两者之间的数字之后。
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i]+ dp[i-1]
        count = 0
        for i in range(len(dp)):
            # 可能单独到i个位置时出现为k也需要+1
            if dp[i]==k:
                count+=1
            for j in range(i+1,len(dp)):
                if dp[j]-dp[i]==k:
                    count+=1
        return count


a = Solution()
nums = [1,1,1]
k = 2
re1 = a.subarraySum(nums, k)
re2 = a.subarrray(nums, k)
print(re1, re2)