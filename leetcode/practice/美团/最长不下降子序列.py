# encoding: utf-8
# ------------ 美团 ---------------
# 最长不下降子序列：将序列去除最少的数后，序列内每一个数都大于等于前面的数
# e.g. 10011 去除第一个数后，最长不下降子序列0011，长度为4
# 现在有二进制序列，进行修改操作并询问最长不下降子序列长度
# 输入
# 5 5    序列长度n = 5；操作次数m = 5
# 10011  序列
# q      询问整段序列的最长不下降子序列长度
# c 1 5  将序列区间[1,5]的0变1，1变0
# q      询问整段序列的最长不下降子序列长度
# c 1 3  将序列区间[1,3]的0变1，1变0
# q      询问整段序列的最长不下降子序列长度
# # 输出
# 4      原序列 10011 最长不下降子序列为 0011，长度为4
# 3      原序列 10011 修改后 01100 最长不下降子序列为 011/000，长度为3
# 4      原序列 01100 修改后 10000 最长不下降子序列为 0000，长度为4

import sys


# --------- 动态规划  ----------------
# 不下降子序列之间是跳跃的
# 每一次询问都是最新序列，每一次修改针对最新序列

def lengthOfLIS(arr):
    dp = [1] * len(arr)  # 从0开始，以第i个数字结尾的最长子序列长度
    for i in range(1, len(arr)):  # 删除一个元素，所以到不了最后一个位置
        if arr[i-1] == "0" or arr[i] == arr[i-1]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, m = tmp[0], tmp[1]
    str = sys.stdin.readline().strip()
    arr = [str[i:i + 1] for i in range(0, n, 1)]  # 替换指定位置的字符
    res = []
    for i in range(m):
        tmp = list(sys.stdin.readline().strip().split(' '))
        if tmp[0] == "q":
            length = lengthOfLIS(arr)
            res.append(length)
        else:
            for j in range(int(tmp[1])-1, int(tmp[2])):
                arr[j] = "0" if arr[j] == "1" else "1"

    for i in range(len(res)):
        print(res[i])


main()
