# 75. Sort Colors

![image-20200418154223673](../../../.assert/image-20200418154223673.png)

给定一个数组，只包含0，1，2，对其进行排序，使得顺序为0，1，2.

## 复制

遍历一遍数组，记录0，1，2的个数，然后写入原数组中。

时间复杂度为O(N)但是需要遍历两边

## 遍历一遍

利用三个指针分别指向头头尾

第一个指针记录0数组最后的位置

第三个指针记录2数组第一个位置

第二个指针遍历中间的值，与第一个第三个指针进行交换。

~~~python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two = 0, len(nums)-1
        while zero <= two and nums[zero] == 0:
            zero += 1
        while two >= zero and nums[two] == 2:
            two -= 1
        i = zero
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero+=1
                i+=1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
            else:
                i += 1
~~~

