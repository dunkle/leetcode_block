class Solution:
    def largestRectangleArea(self, heights) -> int:
        '''
        在首尾两处加入两个哨兵，避免一直处于递增状态，遍历结束数组，栈中仍然存在元素
        '''
        heights = [0]+ heights+ [0]
        n = len(heights)
        stack = [0]
        maxnum = 0
        for i in range(1, n):
            # 维护一个单调栈，柱状图从左往右
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                maxnum = max(maxnum, width*height)
                # print(maxnum)
            stack.append(i)
            # print(stack)
            # print(heights[stack[-1]])
        return maxnum