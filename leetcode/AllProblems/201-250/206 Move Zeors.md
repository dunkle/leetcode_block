# 283. Move Zeroes

![image-20200404173427154](../../.assert/image-20200404173427154.png)

给定一个数组将0都放到数组的后面

## 方法1

创建一个auxiliary数组，遍历一遍原数组将非0数放到auxiliary中，然后复制回去。时间复杂度为$O(N)$,空间复杂度为$O(N)$

~~~python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        auxiliary = [0] * len(nums)
        i = 0
        for n in nums:
            if n != 0:
                auxiliary[i] = n
                i += 1
        nums[:] = auxiliary[:]
~~~

## 方法2

用一个变量记录上一个0的位置，找到下一个非零数，交换二者。时间复杂度为$O(N)$,空间复杂度为$O(1)$

~~~python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, last_zero = 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_zero] = nums[last_zero], nums[i]
                last_zero+=1
~~~

