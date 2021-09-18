class Solution:
    def largestRectangleArea(self, heights) -> int:
        '''
        1、设置一个单调递增栈，保存的是递增heighs对应的index
        2、当新遍历的height比stack最后一个元素小，需要弹出栈
        3、因为后续高度即使再高，构成的矩形面经也是小于当前height的高度
        4、统计计算一下当前位置i到 弹出的height的面积。 最高高度就是当前i处的height，宽度i-index-1

        技巧：在首尾两处加入两个哨兵，避免一直处于递增状态，遍历结束数组，栈中仍然存在元素
        '''
        heights = [0]+ heights+ [0]
        n = len(heights)
        stack = [0]
        maxnum = 0
        for i in range(1, n):
            # 维护一个单调栈，柱状图从左往右
            # print(list(map(lambda x: heights[x],stack)))
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                maxnum = max(maxnum, width*height)
                # print(maxnum)
            stack.append(i)
            # print(stack)
            # print(heights[stack[-1]])
        return maxnum

a = Solution()
heights = [2,1,5,6,2,3]
res = a.largestRectangleArea(heights)
print(heights)
print(res)