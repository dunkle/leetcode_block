# encoding: utf-8
# 请使用标准输出(sys.stdout)；勿使用图形、文件、网络、系统相关的操作，如Process , httplib , os
# 缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
# 如果使用sys.stdin.readline，因为默认会带换行符，所以要strip(' ')进行截取；建议使用input()

# ------------ 美团 ---------------
# 无限大的二维平面内，每个星星是一个点，若一颗星星的上下左右都有其他的星星，则为幸运星，求区域内有多少幸运星
# 输入：
# 8     # 星星总数n = 8
# 0 0   # 第一颗星星的坐标
# 0 1
# 0 2
# 0 3
# 1 1
# 1 2
# -1 1
# -1 2
# 输出
# 2      # 两颗幸运星：（0，1）；（0，2）
import sys
# ------------- dict + set ----------------------

def main():
    n = int(input())
    star_x = {}
    star_y = {}
    for i in range(n):
        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        if tmp[0] in star_x:
            old = star_x[tmp[0]]
            new = old + [tmp[1]]
            star_x[tmp[0]] = new
        else:
            star_x[tmp[0]] = [tmp[1]]
        if tmp[1] in star_y:
            old = star_y[tmp[1]]
            new = old + [tmp[0]]
            star_y[tmp[1]] = new
        else:
            star_y[tmp[1]] = [tmp[0]]
    tmp_y = set()  # 遍历横坐标，set记录幸运星可能的纵坐标
    # set 存储不重复值，add更新一个；update更新多个
    for key in star_x:
        if len(star_x[key]) > 2:
            # 从索引为0的列表元素开始迭代列表至索引为 len(star_x[key])-2 的列表元素
            tmp_y.update(star_x[key][1:len(star_x[key])-1])
    res = 0
    while tmp_y:
        tmp = tmp_y.pop()
        if len(star_y[tmp]) > 2:
            res += len(star_y[tmp]) - 2
    print(res)


if __name__ == '__main__':
    main()
