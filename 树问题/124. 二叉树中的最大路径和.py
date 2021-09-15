class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        '''
        最大路径和包括两种：
        a/ 包括 当前根节点root+左节点+右节点， 则根节点的父节点的值暂不考虑。
            此处接入 全局变量，从叶子节点网上递归，无法知道包含当前根节点的值是否为最大值
        b/ 包括 左节点/右节点之间的一个（取最大）， 包括根节点，往上递归根节点的父节点
            root + max(left, right) （此处返回时，代表了路径往上递归的子树中的最大的路径）
            如果左右节点的值为负，则可以直接舍去，取0
        '''
        self.sumall = 0
        def recur(root):
            if not root:
                return 0
            # 左子树最大路径，如果小于0直接为0不取
            left = max(recur(root.left), 0)
            right = max(recur(root.right),0)
            # 同时包含左右路径的情况，不需要再递归，因此作为最终路径和的值进行比较
            self.sumall = max(self.sumall, left+right+root.val)
            # 递归左右子树，选择最大的一条路径继续递归
            return max(left, right) + root.val
        recur(root)
        return self.sumall
