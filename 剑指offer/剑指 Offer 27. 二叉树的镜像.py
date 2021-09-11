class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        '''
        # 递归法
        依次递归得到左右子树节点,然后交换
        '''
        if not root:
            return
        # 一直递归获得左节点和右节点
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)
        # 把这两个对称节点交换
        root.left, root.right = root.right, root.left
        return root
    def mirrorTree1(self, root: TreeNode) -> TreeNode:
        '''
        迭代法
        '''
