给定一个包含重复元素的数组，求出所有子集。

 ![image-20201008162326958](../../../.assert/image-20201008162326958.png)



与不包含重复元素的类似，采用迭代的方式计算。但是要注意处理重复值，如果有重复值，那么与其他元素的组合只需要计算一遍。

首先进行排序，让相同的元素相邻。用一个数组保存每一轮迭代的结果，如果当前元素与上一轮相同，则只与上一轮的结果组合即可，如果不相同，则与结果集中所有的元素组合。

~~~python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        cur = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [sub + [nums[i]] for sub in cur]
            else:
                cur = [sub + [nums[i]] for sub in result]
            result += cur
        return result
~~~

