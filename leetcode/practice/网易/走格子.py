# encoding: utf-8
# ------------ 网易 ---------------
# 网格n✖️m，小强从起点走到终点，每一步可选择周围8个点
# 网格内有发射器，发出的激光为某一方向直线，到下一个发射器或障碍物停止
# 网格内的障碍物不可通过
# 要求最终的路径中相邻两个格子最多有一个格子有激光
# 求路径最少有几个格子有激光，若路径不存在返回-1
# 输入
# 2           一共T组测试数据，T = 2
# 3 3         第一组测试用例   网格大小 n = 3; m = 3
# 1 1 3 3                    起点坐标和终点坐标 x1 = 1；y1 = 1；x2 = 3；y2 = 3
# 2                          有k个障碍物和发射器 k = 2
# 2 1 r                      发射器坐标，方向向右（u：上；d：下；l：左）
# 2 3 B                      障碍物坐标
# 3 2         第二组测试用例   网格大小 n = 3; m = 2
# 1 2 3 1                    起点坐标和终点坐标 x1 = 1；y1 = 2；x2 = 3；y2 = 1
# 2                          有k个障碍物和发射器 k = 2
# 2 1 B                      第一个障碍物坐标
# 2 2 B                      第二个障碍物坐标
# 输出
# 1           第一组测试用例   有一个格子有激光
# -1          第二组测试用例   路径不存在
# --------- DFS  -------------------
# 禁止：边界；障碍物；连续两个激光格子
# 终止：终点；
# 剪枝：当前激光格子多于之前
import sys


def main():
    T = int(sys.stdin.readline().strip())  # T 组测试
    res = [0] * T # 每组测试的结果
    for i in range(T):
        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        n, m = tmp[0], tmp[1]   # 网格大小
        res[i] = n * m

        # net = [[1] * (m + 1)] * (n + 1)
        # 本意是把矩阵的第一行第二列赋值为 2， 但是最终结果是每一行的第二列都是 2
        # ist * n—>n shallow copies of list concatenated, n个list的浅拷贝的连接
        # 修改其中的任何一个元素会改变整个列表，
        net = [([0] * (m + 1)) for x in range(n + 1)]  # 变量 i 不能重复
        # 行数：n + 1；列数：m + 1，是为了和之后的格子坐标对应
        # 在网格中可以通过：0，激光格子：1；障碍物：-1，是为了记录路径中总激光格子数可以直接加上net值

        tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
        x1, y1, x2, y2 = tmp[0], tmp[1], tmp[2], tmp[3]         # 起点；终点

        k = int(input())   # 激光+障碍物数量
        x = [0] * k  # 激光横坐标list
        y = [0] * k  # 激光纵坐标list
        laser = [0] * k  # 激光类型

        # 首先在网格中表示出障碍物 0
        for j in range(k):
            tmp = sys.stdin.readline().strip().split(' ')
            if ord(tmp[2]) == 66:  # B: 障碍物
                net[int(tmp[0])][int(tmp[1])] = -1
            else:
                x[j], y[j], laser[j] = int(tmp[0]), int(tmp[1]), ord(tmp[2])

        # 根据障碍物和边界，在网格中表示出激光格子 -1
        j = 0
        while laser[j] and j < k:
            if laser[j] == 114:  # r: 👉
                r = 0
                while (y[j] + r) <= n and net[x[j]][y[j] + r] != -1:  # 没有越界和障碍物
                    net[x[j]][y[j] + r] = 1  # 激光格子
                    r += 1
            elif laser[j] == 108:  # l: 👈
                r = 0
                while (y[j] - r) > 0 and net[x[j]][y[j] - r] != -1:  # 没有越界和障碍物
                    net[x[j]][y[j] - r] = 1  # 激光格子
                    r += 1
            elif laser[j] == 117:  # u: 👆
                r = 0
                while (x[j] - r) > 0 and net[x[j] - r][y[j]] != -1:  # 没有越界和障碍物
                    net[x[j] - r][y[j]] = 1  # 激光格子
                    r += 1
            else:
                r = 0
                while (x[j] + r) <= m and net[x[j] + r][y[j]] != -1:  # 没有越界和障碍物
                    net[x[j] + r][y[j]] = 1  # 激光格子
                    r += 1
            j += 1

        # ------------- DFS -------------
        stack = [(x1, y1),(0, 0)]  # 沿途格子压栈
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        path = []  # 该路径不存在
        laser = 0  # 该路径的激光格子数量，用于剪枝和选择最优答案
        while stack:
            stack.pop()  # 第一次pop是(0, 0) 表示当前的层次
            if not stack:  # 此时path也为空
                break
            cur_x, cur_y = stack.pop()           # 第二次pop是此次要走的格子
            stack.append((0, 0))                 # 将(0, 0) 加上，使得实际上每次只pop了第二次的值
            if cur_x:                            # 此次要走的格子是有实际位置的
                laser += net[cur_x][cur_y]       # 假设走这个格子，首先加上这个格子的net值
                if laser <= res[i]:              # 假设成立
                    path.append((cur_x, cur_y))  # 将格子加入path
                    for j in direction:          # 寻找这个格子的下一个合理的格子
                        if 0 < cur_x + j[0] <= n and 0 < cur_y + j[1] <= m \
                                and net[cur_x + j[0]][cur_y + j[1]] != -1 \
                                and net[cur_x][cur_y] + net[cur_x + j[0]][cur_y + j[1]] < 2 \
                                and (cur_x + j[0], cur_y + j[1]) not in path:  # # 边界, 障碍物,相邻两个格子最多有一个格子有激光
                            if cur_x + j[0] == x2 and cur_y + j[1] == y2:  # 终点不入栈
                                laser += net[cur_x + j[0]][cur_y + j[1]]   # 确定整个路径的激光格子数量
                                if res[i] > laser:                         # 和之前的最优值比较
                                    res[i] = laser                         # 更新
                            else:                                          # 不是终点
                                stack.append((cur_x + j[0], cur_y + j[1])) # 入栈
                    stack.append((0, 0))      # 每一轮确定后续格子后，都加入(0, 0)表示一个层级
                else:                         # 需要剪枝，将laser复原
                    laser -= net[cur_x][cur_y]
            else:                             # 两次pop都是0，说明path需要回溯一个层级
                tmp = path.pop()
                laser -= net[tmp[0]][tmp[1]]  # laser与path保持一致
        if res[i] == m*n:  # res[i]从未做更新，说明遍历完全也没有找到路径
            res[i] = -1    # 路径不存在，返回-1
    for i in range(T):     # 返回每一组测试的结果
        print (res[i])


main()
