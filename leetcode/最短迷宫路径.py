#coding=utf-8
import sys
#str = input()
#print(str)


def shortestPath(martrix):
    m = len(martrix)
    n = len(martrix[0])
    def isval(x,y):
        if 0<=x<m and 0<=y<n:
            return True
        return False
    def is_visit(x,y):
        if martrix[x][y]==1:
            return True
        return False
    queue = [[0,0,0]]
    res = 1
    dis = [[0 for i in range(n)] for j in range(m)]
    while queue:
        node = queue.pop()
        steps = [(-1,0),(0,1),(1,0),(0,-1)]
        martrix[node[0]][node[1]]=1
        print("res:",res, queue)
        if node[0]==m-1 and node[1]==n-1:
            break
        for step in steps:
            x = step[0]+node[0]
            y = step[1]+node[1]
            # 可达位置 判断
            if isval(x, y) and not is_visit(x, y):
                queue.append([x,y,res])
                dis[x][y] = dis[node[0]][node[1]]+1
                martrix[x][y]=1
    return dis[m-1][n-1]+1
martrix = [[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[1,0,1,1,1],[1,0,0,0,0],[0,0,0,1,0]]
martrix = [[0,0,0,0],
           [0,1,0,0],
           [0,0,0,0],
          [1,0,1,0],]
result = shortestPath(martrix)
print(result)

