class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def is_same(A,B):
            if not B:
                return True
            if not A or A.val!=B.val:
                return False
            return is_same(A.left, B.left) and is_same(A.right, B.right)
        def recur(A, B):
            if not A or not B:
                return False
            if A.val==B.val:
                if is_same(A,B):
                    return True
            return recur(A.left, B) or recur(A.right, B)