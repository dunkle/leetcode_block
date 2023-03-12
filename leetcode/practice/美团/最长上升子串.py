# encoding: utf-8
# ------------ 美团 ---------------
# 从长度为n的正整数构成的序列中删去一个数后，可求该序列的最长上升子串
# 求任意的删除方案中，最长上升子串
# 最长上升子串：长度最长的上升子串
# 上升子串：序列中连续的若干递增
# 输入
# 5            # n = 5
# 2 1 3 2 5    # 序列
# 输出
# 3            # 最长上升子串的长度（删除3后，最长上升子串：1，2，5）
import sys


# --------- 动态规划  ----------------
# 删除第i个数字，则需要求nums[0:i]和nums[i+1:]
# 遍历所有删除位置，求max

def lengthOfLIS(nums):
    dp_end = [1] * len(nums)  # 从0开始，以第i个数字结尾的最长子序列长度
    for i in range(1, len(nums)):  # 删除一个元素，所以到不了最后一个位置
        if nums[i - 1] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
            dp_end[i] = max(dp_end[i], dp_end[i - 1] + 1)
    return max(dp_end)


def main():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split(' ')))
    res = 0
    for i in range(n):
        tmp = lengthOfLIS(nums[0:i] + nums[i + 1:])
        if tmp > res:
            res = tmp
    print(res)


main()
