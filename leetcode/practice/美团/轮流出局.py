# encoding: utf-8
# ------------ 美团 ---------------
# n个人（编号：1～n）进行n轮报数，报数从0开始
# 每轮都从编号为1的人开始，若1出局，则以此类推
# 第i轮报到A[i]（可能大于当前剩余人数）的人出局，此轮游戏结束
# 第一轮出局的选手排名倒数第一，第i轮出局的排名n-i+1
# 按编号输出每个人的排名
# 输入
# 4         # n个人
# 1 2 1 2   # A
# 输出
# 1 4 2 3
# 第1轮：1：0；2：1=A[i]，出局，排名为4
# 第2轮：1：0；3：1；4：2=A[i]，出局，排名为3
# 第3轮：1：0；3：1=A[i]，出局，排名为2
# 第4轮：1：0；1：1=A[i]，出局，排名为1
import sys


def main():
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split(' ')))
    people = [i for i in range(n)]   # index为i的人报数i
    rank = [0]*n                    # 每个人 index - ranking
    for i in range(n):              # 每一轮报数，一个人出局，确定其排名
        # 停止的数值A[i]若大于现存人数，由于报数是累加的，A[i]最终落在people的索引为index位置
        index = A[i] % len(people)
        # 此轮出局的人为 people.pop(index)，排名为n - i
        rank[people.pop(index)] = n - i
    print(rank)


main()
