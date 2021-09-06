class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode):
        queue = [root]
        res = []
        if not root:
            return []
        # 二叉树的右视图，本质上就是层序遍历，最右边的元素
        while queue:
            n = len(queue)
            # 把最右边的元素加入res
            res.append(queue[-1].val)
            for i in range(n):
                # 先放左边的元素，并且先弹出左边的元素
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
