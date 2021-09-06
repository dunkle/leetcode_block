class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        '''
        颜色标记法， 中序遍历 左 中 右
        实际栈保存 应该是逆序保存 右 左 中
        :param root:
        :return:
        '''
        WHITE, GRAY = 0, 1
        res = []
        # 白色 代表未访问 灰色代表已访问
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def inorder2(self, root):
        '''
        white对应TreeNode数据类型，gray对应int数据类型，所以不需要额外的颜色标记：
        :param root:
        :return:
        '''
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                # 把要先访问的点 存为 int类型，其他存为 node 类型
                stack.extend([i.right,i.val,i.left])
            elif isinstance(i,int):
                rst.append(i)
        return rst