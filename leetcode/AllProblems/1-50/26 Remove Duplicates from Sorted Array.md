# 26. Remove Duplicates from Sorted Array

![image-20200330023238537](../../../.assert/image-20200330023238537.png)

给定一个已排序的数组，移除其中所有重复的元素。

![image-20200330023319693](../../../.assert/image-20200330023319693.png)

由于数组是排序的，因此可以用两个指针，一个指针指向当前唯一的值，另一个指针向下遍历找到下一个与当前值不同的值。

~~~python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        current, next_pos = 0, 0
        while next_pos < len(nums):
            while next_pos < len(nums) and nums[current] == nums[next_pos]:
                next_pos += 1
            if next_pos < len(nums):
                nums[current+1] = nums[next_pos]
                current += 1
        return current + 1
~~~

