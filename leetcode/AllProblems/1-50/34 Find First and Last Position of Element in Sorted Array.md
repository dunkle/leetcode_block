给定一个包含重复元素的有序数组，求出给定`target`的边界index。

使用两次二分查找，第一次查找左边界，第二次查找右边界。

二分查找跳出循环的条件为`left <= right`,因此最终只可能有一种情况`left=right+1`，当target与mid值相等时，会不断收缩右边界，最终left指向的位置就是左边界。

对于目标不在数组中的情况，left可能有三种位置：

1. taget比nums中的数都小，left=0，right=-1，此时可直接判断nums[left]不等于target
2. target比nums中的数都大，left=len(nums)，right=len(nums)-1，此时可判断left的位置
3. target在范围中间但不存在，此时直接判断nums[left]不等于target

其中1，3可以合并，2判断边界即可。

对于查找右边界同理，通过收缩left，定位右边界的位置，最终right指向的就是右边界。

~~~python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return -1, -1
        left_index, right_index = -1, -1
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1, -1
        
        left_index = left
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = mid + 1
        right_index = right
        return left_index, right_index
~~~

