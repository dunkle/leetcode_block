class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        对称二叉树定义： 对于树中 任意两个对称节点 LL 和 RR ，一定有：
        L.val = R.valL.val=R.val ：即此两对称节点值相等。
        L.left.val = R.right.valL.left.val=R.right.val ：即 LL 的 左子节点 和 RR 的 右子节点 对称；
        L.right.val = R.left.valL.right.val=R.left.val ：即 LL 的 右子节点 和 RR 的 左子节点 对称。

        :param root:
        :return:
        '''
        if not root:
            return True
        def recur(L, R):
            # 传递进来左右子树 如果为空说明到达叶子节点
            if not L and not R:
                return True
            # L R 不同时为空，那么如果有一个为空 或者 都不为空值不等 false
            if not L or not R or L.val!=R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        return recur(root.left, root.right)
