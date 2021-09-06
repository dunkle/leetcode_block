class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

    # 原地hash算法，上述算法时间和空间复杂度都是 O(n)
    def findRe(self, nums):
        i = 0
        # 肯定能找到
        while 1:
            # 如果下标和当前位置对应的值相等，则代表一致，继续往前
            if i == nums[i]:
                i += 1
                continue
            else:
                # 如果不一致，则以当前位置值 去索引该位置的指向的值，如果相等，说明重复
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                else:
                    # 如果不等，则替换掉该位置为相等的值。
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


a = Solution()
# nums = [2, 3, 1, 0, 2, 5, 3]
nums = [1, 3, 5, 4, 7, 2, 6, 3]
# res = a.findRepeatNumber(nums)
# print(res)
res2 = a.findRe(nums)

print(res2)
