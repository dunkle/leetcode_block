# 二叉树的层次遍历 返回每一层的最大值
# 输入root, 返回list

def findmax(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        tmp = []
        # 当前层有多少个节点
        for i in range(len(queue)):
            # 每个节点依次弹出，把值存在tmp里
            node = queue.pop()
            tmp.append(node.val)
            # 下一层
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(max(tmp))
    return res

