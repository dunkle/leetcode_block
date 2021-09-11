# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 树结构为空，
        if not root:
            return False
        def recur(root, nowsum):
            # print(nowsum)
            nowsum+=root.val
            left, right = False, False
            # 如果是到达了叶子节点，判断求和是否等于目标值
            if not root.left and not root.right:
                return nowsum==targetSum
            # 如果左右节点不为空，递归判断
            if root.left:
                left = recur(root.left, nowsum)
            if root.right:
                right=  recur(root.right, nowsum)
            # 左右子树是否存在包含 路径和为 目标值的情况，因此为或
            return left or right
        return recur(root, 0)