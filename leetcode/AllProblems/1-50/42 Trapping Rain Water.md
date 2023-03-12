![image-20210117123553050](../../../.assert/image-20210117123553050.png)

给定一个直方图，问中间能接到多少雨水。

## 方法一

在每个点的位置，向左寻找左边的最大值，向右寻找右边的最大值，则当前位置能接雨水的数量为二者的最小值。

时间复杂度为$O(N^2)$

空间复杂度为$O(1)$

## 方法二

方法一需要在每个点都算出左边和右边的最大值最小值，但这个值可以提前计算出来。

~~~python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left_max = [x for x in height]
        right_max = [x for x in height]
        
        l = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(l, height[i])
            l = left_max[i]
        r = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(r, height[i])
            r = right_max[i]
        ans = 0
        for i in range(1, len(height)-1):
            ans += min(left_max[i], right_max[i]) - height[i]
            
        return ans
~~~

## 方法三

相比较方法二用两个数组分别记录左边的最大值和右边的最大值，可以用一个栈来记录左边的最大值，也即单调栈的用法。

- 用栈来保存每个直方图的序号
- 遍历数组
  - 如果$\text{height[current]}>\text{height[st.top()]}$
    - 说明当前遍历的直方图和栈中的某一个元素可以将栈顶元素界定，栈顶元素可以弹出，可以计算出栈顶元素存放的水滴数量
    - 可存放水滴的宽度为current-st.top()-1
    - 可存放水滴的高度为min(height[current],height[st.top()])−height[top]
    - ans += height + distance
  - 将当前元素入栈

~~~python
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while len(stack) > 0 and h > height[stack[-1]]:
                topi = stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                bound_height = min(h, height[stack[-1]]) - height[topi]
                ans += distance * bound_height
            stack.append(i)
            
        return ans
~~~

​    时间复杂度为$O(N)$,空间复杂度为$O(N)$

## 方法四

双指针

~~~python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_max, right_max, ans = 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
~~~

