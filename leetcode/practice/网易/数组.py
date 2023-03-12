# encoding: utf-8
# ------------ 网易 ---------------
# 一个长度为n的递增数组，数组内每个元素，后一个减前一个是d的倍数
# 寻找最大的正整数d，d不存在输出-1
# 输入
# 4         # n个数
# 1 3 7 15
# 输出
# 2
import sys


# ---------- 辗转相除 ----------------
def gcd(p, q):  # 欧几里得算法递归实现最大公约数
    if q == 0:
        return p
    return gcd(q, p % q)


def main():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    arr[0] = arr[1] - arr[0]
    res = arr[n - 1]
    for i in range(2, n):
        arr[i - 1] = arr[i] - arr[i - 1]
        print (arr)
        tmp = gcd(arr[i - 1], arr[i - 2])
        print (tmp)
        if tmp < res:
            res = tmp
    if res == arr[n - 1]:
        res = -1
    print(res)


main()
