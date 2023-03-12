# 详细描述
# 一个机器人要从起始点A和终点B。机器人从起点开始，每次能从上，下，左，右移动一步通过一个房间。并且每个房间只能路过一次。
# 设定机器人的健康数为H，如果经过的房间是正整数a，那么机器人经过这个房间就能获得对应的健康点数，健康数变成H+a，如果经过的房间为负数，那么机器人就会失去对应的健康点数a， 机器人的健康数变成H-a，问如果要保证机器人生命数一直是正数，H初始值至少为多少？
# 房间点数由一个二维数组M*N 表示，起点和终点由一个一维数组组成。
# 1 <= M,N <= 200
# m == rooms.length
# n == rooms[i].length
# -1000 <= rooms[i][j] <= 1000
# 0 <= i,j <= M,N
class Solution:
    def __init__(self):
        self.rooms = None
        self.row = 0
        self.col = 0
        self.start = None
        self.end = None
        self.res = []
        self.temp = []
        self.visited = None

    def dfs(self, i, j):
        # if i < 0&nbs***bsp;j < 0&nbs***bsp;i >= self.row&nbs***bsp;j >= self.col&nbs***bsp;self.visited[i][j]:
        #     return
        self.visited[i][j] = True
        if self.temp:
            self.temp.append(self.temp[-1] + self.rooms[i][j])
        else:
            self.temp.append(self.rooms[i][j])
        if self.end == [i, j]:
            self.res.append(min(self.temp))
            self.temp.pop()
            self.visited[i][j] = False
            return
        for x, y in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
            self.dfs(x, y)
        self.temp.pop()
        self.visited[i][j] = False
        return

    def minimumInitHealth(self, rooms, startPoint, endPoint):
        # write code here
        if isinstance(rooms[0], int):
            return abs(rooms[0]) + 1 if rooms[0] < 0 else 1
        self.rooms = rooms
        self.col = len(rooms[0])
        self.row = len(rooms)
        self.end = endPoint
        self.visited = [[False for i in range(self.col)] for j in range(self.row)]
        self.dfs(startPoint[0], startPoint[1])
        min_health = max(self.res)
        return abs(min_health) + 1 if min_health < 0 else 1