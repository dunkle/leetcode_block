class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def recur(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if root.left and root.right:
                return min(recur(root.left)+1, recur(root.right)+1)
            if not root.left:
                return recur(root.left)+1
            if not root.right:
                return recur(root.right)+1
        return recur(root)
    