# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
#       [0,1,0,1,0,0,1,1,0,0,1,0]
# 输出: 6

# 连续的右边比左边高则以左边最小值为底
def trap(height):
    n = len(height)
    if n<2:
        return 0
    left =0
    right = n-1
    heig = 1
    temp = 0
    Sum =0
    while left<=right:
        if height[left] < heig:
            Sum += height[left]
            left+=1
            continue
        if height[right] < heig:
            Sum += height[right]
            right-=1
            continue
        temp = temp + right-left+1
        heig+=1
    return temp-Sum

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([0,2,0]))
print(trap([2,0,2]))