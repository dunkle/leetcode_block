# 189. Rotate Array

![image-20200401122906867](../../.assert/image-20200401122906867.png)

将数组旋转

## 空间换时间

时间复杂度为$O(N)$,空间复杂度为$O(N)$

~~~python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = []
        for i in range(len(nums)-k, len(nums)):
            tmp.append(nums[i])
        for i in range(len(nums)-k):
            tmp.append(nums[i])
        for i in range(len(nums)):
            nums[i] = tmp[i]
~~~

## 位置公式

每一个位置交换后的位置为$(n+k)\%l$,因此，可以利用这个公式不断交换位置，需要注意的地方是要记录每次交换开始的位置，将开始的位置替换完后进行下一轮替换。

![Rotate Array](../../.assert/189_Rotate_Array.png)

~~~python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = nums[0]
        count = 0
        start = 0
        while count < len(nums):
            pos = start
            pre = nums[pos]
            while True:
                next_pos = (pos+k)%len(nums)
                tmp = nums[next_pos]
                nums[next_pos] = pre
                pre = tmp
                pos = next_pos
                count += 1
                # print(nums)
                if pos == start:
                    break
            start += 1
~~~

