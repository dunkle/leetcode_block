# 11. Container With Most Water

![image-20200412125816305](../../../.assert/image-20200412125816305.png)

给定一些垂直长条的高度，计算任意两个长条围起来的最大面积。

## 暴力

用两个指针，从当前指针开始向后找围成最大面积的指针。

~~~python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, max_left = -1, 0
        left, right = 0, 0
        while left < len(height) :
            if height[left] < height[max_left]:
                continue
            for right in range(left, len(height)):
                area = (right - left) * min(height[left], height[right])
                if area > max_area:
                    max_area = area
                    max_left = height[left]
            left += 1
        return max_area
~~~

时间复杂度为$O(N^2)$

## 两个指针

初始化两个指针，分别指向第一个和最后一个。每次向前移动一次高度较短的指针位置。

这么做有效的原因是，因为边长是根据较短长条长度决定的，如果移动长指针，那么宽度会减小，同时高度不会高于长长条的高度，所以只能移动短长条指针，使宽度的减少量通过高度来弥补回来。

~~~python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
~~~

