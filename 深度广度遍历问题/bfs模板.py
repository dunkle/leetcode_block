def bfs(start, target):
    '''
    给定一个起始节点，要求搜索到目标节点，或者目标状态
    :param start:
    :param target:
    :return:
    '''
    import collections
    # 初始化一个队列
    deque = collections.deque()
    # 将bfs 初始化的起点加入
    deque.append(start)
    # 为了避免bfs 不走回头路，定义一个已访问节点库
    visited = set()
    visited.add(start)
    # 定义当前的层数，可以为距离定义，深度定义
    level = 0
    while deque:
        # 记录一下当前层有多少节点
        level_lenth = len(deque)
        # 依次遍历当前层的节点
        for _ in range(level_lenth):
            node = deque.popleft()
            # 如果当前节点是目标状态或者目标节点，返回
            if node is target:
                return level
            # 如果当前节点不是目标节点，则将与该节点相邻的节点都放入队列中
            for nodenext in node:
                # 只有当前节点没被遍历过才放入队列
                if nodenext not in visited:
                    deque.append(nodenext)
                    visited.add(nodenext)
        level+=1
    return level