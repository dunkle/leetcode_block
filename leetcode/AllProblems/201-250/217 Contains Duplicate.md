# 217. Contains Duplicate

**Hash**

~~~python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        return not all(x == 1 for x in c.values())
~~~

没要每个值都统计

~~~python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False
~~~

可以直接利用set算

~~~python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return not len(set(nums)) == len(nums)
~~~

