# 1. Two Sum

## 暴力

## 使用hashtable

~~~
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            sub = target - num
            if sub in d:
                return [i, d[sub]]
            else:
                d[num] = i
~~~

## 二分查找

这里要注意两个问题：

1. 题目要求的是求出数对的下标，而且是在原数组中的下标，因此排序之后要在原序列中找下标
2. 数组中是由重复元素的，因此找到两个数的下标时要判断是否相等，相等的话要找下一个

~~~python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def in_nums(nums, n, start, end):
            if end < start:
                return -1
            mid = (start + end) // 2
            # print(start, mid, end)
            if nums[mid] == n:
                return mid
            if nums[mid] > n:
                return in_nums(nums, n, start, mid-1)
            else:
                return in_nums(nums, n, mid+1, end)
        b_nums = nums.copy()
        nums = sorted(nums)
        for i, n in enumerate(nums):
            t = in_nums(nums, target-n, i+1, len(nums)-1)
            if t != -1:
                a = b_nums.index(n)
                b = b_nums.index(target-n)
                if a == b:
                    b = b_nums[a+1:].index(target-n) + a + 1
                return a, b
            
         
~~~

为了记住元素在数组中的位置，可以创建一个新的list，内容为值和index的元组

注意在对有序数组进行二分查找的时候是在当前元素之后的数组查找

~~~python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def helper(nums, n):
            if len(nums) == 0:
                return None
            mid = (len(nums)-1)//2
            if nums[mid][0] == n:
                return nums[mid]
            elif nums[mid][0] < n:
                return helper(nums[mid+1:], n)
            else:
                return helper(nums[:mid], n)
        
        nums = [(x, i) for i, x in enumerate(nums)]
        nums = sorted(nums, key=lambda x:x[0])
        for i, tt in enumerate(nums):
            n, index = tt
            t = helper(nums[i+1:], target-n)
            if t is not None:
                return (index, t[1])
~~~

