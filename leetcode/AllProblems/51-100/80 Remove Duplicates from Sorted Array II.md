![image-20201006215142281](../../../.assert/image-20201006215142281.png)

给定一个有序数组，其中包含重复值，去除重复的数字，使每个数字出现的次数不超过两次。

两个变量，分别记录当前重复的数字和重复的次数。

~~~python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curn, curtimes = nums[0], 1
        i, j = 1, 1
        while j < len(nums):
            if nums[j] == curn:
                if curtimes < 2:
                    nums[i] = nums[j]
                    i += 1
                    curtimes += 1
            else:
                nums[i] = nums[j]
                i += 1
                curn, curtimes = nums[j], 1
            j += 1
        return i
                    
             
~~~

