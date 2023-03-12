# coding=utf-8
# ------------ 美团 ---------------
# 两个人一开始各自有n张牌，每个人选出三张牌，点数之和最大为获胜，求获胜一方的点数之和
# 输入
# 5           # 每个人有5张牌
# 1 2 3 4 5
# 1 2 3 4 6
# 输出
# 13

# -------------- 栈 ------------------
import sys
def main():
    n = int(sys.stdin.readline().strip())  #牌的个数
    first = list(map(int, sys.stdin.readline().strip().split(' ')))
    second = list(map(int, sys.stdin.readline().strip().split(' ')))
    first_stack = [0]*3
    first_stack[0] = min(first[0],first[1], first[2])
    first_stack[2] = max(first[0], first[1], first[2])
    first_stack[1] = first[0] + first[1] + first[2] -first_stack[0]-first_stack[2]
    second_stack = [0] * 3
    second_stack[0] = min(second[0], second[1], second[2])
    second_stack[2] = max(second[0], second[1], second[2])
    second_stack[1] = second[0] + second[1] + second[2] - second_stack[0] - second_stack[2]
    for i in range(3,n):
        if first[i]>first_stack[2]:
            first_stack[0],first_stack[1],first_stack[2] = first_stack[1],first_stack[2],first[i]
        elif first[i]>first_stack[1]:
            first_stack[0], first_stack[1] = first_stack[1], first[i]
        elif first[i]>first_stack[0]:
            first_stack[0] = first[i]

        if second[i] > second_stack[2]:
            second_stack[0], second_stack[1], second_stack[2] = second_stack[1], second_stack[2], second[i]
        elif second[i]  > second_stack[1]:
            second_stack[0], second_stack[1] = second_stack[1], second[i]
        elif second[i]  > second_stack[0]:
            second_stack[0] = second[i]
    first_sum = first_stack[0] + first_stack[1] + first_stack[2]
    second_sum = second_stack[0] + second_stack[1] + second_stack[2]
    if first_sum > second_sum :
        print(first_sum)
    else:
        print(second_sum)

main()
