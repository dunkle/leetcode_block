# 238. Product of Array Except Self

![image-20200403145057913](../../.assert/image-20200403145057913.png)

给定数组nums，求output数组，使得output[i]为除nums[i]之外所有数的乘积。

## 左右乘积数组

由题意可得$\text{output}[i] = \Pi_j^n\text{nums}[j], j\neq i$,因此，可以分别求出当前数左边和右边的乘积二者相乘即可，而做左边和右边的output为$\text{output}[i-1] = \text{output}[i-1]*\text{nums}[i-1]$,右边同理.

因此可以构造两个数组l2r和r2l,分别代表从左至右和从右至左的数的乘积

~~~python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, j = 1, len(nums)-2
        l2r, r2l = [1]*len(nums), [1]*len(nums)
        result = [1] * len(nums)
        while i < len(nums):
            l2r[i] = nums[i-1] * l2r[i-1]
            r2l[j] = nums[j+1] * r2l[j+1]
            i, j = i+1, j-1
        for i in range(len(nums)):
            result[i] = l2r[i] * r2l[i]
        return result
~~~

## 空间复杂度O(1)算法

由于最终的结果不算空间，因此可以先用output暂存l2r，然后事实计算r2l

~~~python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]
        R = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] = R * output[j]
            R = nums[j] * R
        return output
~~~

