# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recur(root, p, q):
            # 如果节点值为空，那么直接返回空节点
            # 如果节点值与p或者q任意一个节点一致，那么直接返回当前节点值，最先找到的节点，无论另一个节点是否找到，必定为最近的一个节点
            if not root or root==p or root==q:
                return root
            # 依次递归左右节点
            left = recur(root.left, p, q)
            right = recur(root.right, p, q)
            # 递归结束如果左右节点都为空，那么说明是叶子节点了
            if not left and not right:
                return
            # 如果左节点为空，右节点不为空，说明右边节点已经找到最近的节点
            if not left:
                return right
            if not right:
                return left
            # 如果左右节点都不为空，证明左右节点分叉在当前根节点左右两侧，当前节点为根节点。
            return root
        return recur(root, p, q)