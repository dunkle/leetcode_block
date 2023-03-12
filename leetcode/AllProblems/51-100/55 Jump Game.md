![image-20201006154419199](../../../.assert/image-20201006154419199.png)

给定一个数组，数组的内容是可以移动的长度。判断是否可以从第一个元素移动到最后一个元素。用一个变量记录最后一个可以到达终点的位置，然后从倒数第二个元素开始判断。最后判断是否为0.

~~~python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_true = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= last_true:
                last_true = i
        return last_true == 0
        
~~~



