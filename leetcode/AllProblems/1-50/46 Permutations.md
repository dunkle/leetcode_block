# 46. Permutations

~~~python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = list()
        a = list()
        
        def helper(a, nums, result):
            if len(nums) == len(a):
                result.append(a.copy())
                return
            for n in nums:
                if n not in a:
                    a.append(n)
                    helper(a, nums, result)
                    a.pop()
        
        helper(a, nums, result)
        return result
~~~

从一个数组num中去除N可以用`num[:n]+num[n+1:]`

~~~python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = list()
        a = list()
        def helper(a, nums, result):
            if len(nums) == 0:
                result.append(a)
                return
            for i, n in enumerate(nums):
                helper(a + [n], nums[:i]+nums[i+1:], result)
        helper(a, nums, result)
        return result
~~~

使用python的itertools

~~~python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = itertools.permutations(nums)
        return list(l)
~~~

