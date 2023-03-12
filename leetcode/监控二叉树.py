# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def recur(root):
            if not root:
                return 0
            Rll, Rlll, Rllr =0,0,0
            Rlr, Rlrl, Rlrr = 0,0,0
            Rrl, Rrll, Rrlr = 0,0,0
            Rrr, Rrrl, Rrrr = 0,0,0

            if root.left and root.left.left:
                Rll = recur(root.left.left)
                if root.left.left.left:
                    Rlll = recur(root.left.left.left)
                if root.left.left.right:
                    Rllr = recur(root.left.left.right)
            if root.left and root.left.right:
                Rlr = recur(root.left.right)
                if root.left.right.left:
                    Rlrl = recur(root.left.right.left)
                if root.left.right.right:
                    Rlrr = recur(root.left.right.right)

            if root.right and root.right.left:
                Rrl= recur(root.right.left)
                if root.right.left.right:
                    Rrlr = recur(root.right.left.right)
                if root.right.left.left:
                    Rrll = recur(root.right.left.left)

            if root.right and root.right.right:
                Rrr= recur(root.right.right)
                if root.right.right.left:
                    Rrrl = recur(root.right.right.left)
                if root.right.right.right:
                    Rrrr = recur(root.right.right.right)

            mini = min((1+ Rrl+ Rrr + Rlr+ Rll), recur(root.left)+1+ Rrll+Rrlr+Rrrl+Rrrr, recur(root.right) +1+Rlll+Rllr+Rlrl+Rlrr)
            return mini
        return recur(root)

# a = [0,null,0,null,0,null,0,null,0,0,0,null,null,0,0]
root = TreeNode(0)
