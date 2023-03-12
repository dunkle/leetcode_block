![image-20201006215307040](../../../.assert/image-20201006215307040.png)

给定一个有序旋转数组，其中包含重复的数字，寻找target是否在数组中。

首先判断mid和target是否在同一侧，然后在收缩有边界的时候为了防止跳过target，收缩要更加谨慎。

~~~python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if (nums[mid] <= nums[r]) == (target <= nums[r]):
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r -= 1
                else:
                    l = mid+1
            else:
                if nums[mid] > target:
                    l = mid+1
                else:
                    r-=1
        return False
~~~

