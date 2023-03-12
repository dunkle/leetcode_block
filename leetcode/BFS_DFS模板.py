'''
BFS
不需要知道遍历到哪一层
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)

需要知道遍历到哪一层
level = 0
while queue 不空：
    size = queue.size() #计算每一层有多少个节点
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++;
'''

'''
DFS


'''