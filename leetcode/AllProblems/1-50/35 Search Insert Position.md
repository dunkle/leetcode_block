给定一个有序无重复数组和一个`target`，找到target的插入位置。

跳出循环的条件为`left=right+1`

不断收缩右边界，让right指向第一个小于`target`的值，则跳出循环是`left`指向的就是第一个大于`target`的位置。

~~~python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1
                
        return left
~~~

