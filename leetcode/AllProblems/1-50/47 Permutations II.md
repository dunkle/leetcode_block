有重复值的排列

对nums先进行排序，

~~~python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        def helper(a, nums, result):
            if len(nums) == 0:
                result.append(a)
                return
            
            for i, n in enumerate(nums):
                # 如果与前一个值相同，则不加入到a中
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                
                helper(a+[n], nums[:i]+nums[i+1:], result)
        result = [] 
        helper([], nums, result)
        return result
~~~

