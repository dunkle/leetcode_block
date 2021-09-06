class Solution:
    def findDuplicates(self, nums):
        if not nums:
            return []
        res=[]
        n = len(nums)
        # 1<=num<=n 遍历到 num 则令第 num 个元素变成-num
        for i in range(n):
            num=abs(nums[i])
            # 如果第num个数字已经是负的 说明之前遇到过num 说明num出现两次
            if nums[num-1]<0:
                res.append(num)
            else:
                nums[num-1]=-nums[num-1]
        return res


