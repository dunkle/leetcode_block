class Solution:
    def majorityElement(self, nums) -> int:
        # 暴力法 数组记录次数 时间 空间都是 O(n)
        dict = {}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=0
        return max(dict, key=lambda x: dict[x])
    def majorityElement_(self, nums) -> int:
        # 摩尔投票法
        count =1
        flag = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==flag:
                count+=1
            else:
                if count==0:
                    flag = nums[i]
                    count=1
                else:
                    count-=1
        return flag
