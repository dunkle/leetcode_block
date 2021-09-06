class Solution:
    def threeSum(self, nums):
        '''
        注意两点：
        1、排序之后的数组，依次取第一个数字作为target，那么就不用考虑当前位置以及之前位置作为三数之和之间的一个数字
        2、考虑连续出现相同数字时，
            1）target出现连续重复字符，此时需要在 执行找完target之后，继续将指针后移，保证只出现一次结果
            2）target之后 l出现连续重复字符，需要考虑剔除重复连续字符，设置一个初始的flag进行。
        :param nums:
        :return:
        '''
        nums = sorted(nums)
        print(nums)
        results = []
        if len(nums)<3:
            return results
        i=0
        while i<len(nums):
            target = nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r]+target==0:
                   results.append([target, nums[l], nums[r]])
                   flag = nums[l]
                   l+=1
                   while flag==nums[l] and l<r:
                        l+=1
                elif nums[l]+nums[r]+target<0:
                    l+=1
                else:
                    r-=1
            i+=1
            while i<len(nums) and target==nums[i] :
                 i+=1
        print(results)
        return results
a = Solution()
print("start")
# nums = [-4,-1,0,1,2,-1,-4]
nums = [0, 0, 0]
a.threeSum(nums)