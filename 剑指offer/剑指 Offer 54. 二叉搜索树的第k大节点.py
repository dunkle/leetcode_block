'''
给定一棵二叉搜索树，请找出其中第k大的节点。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        '''
        1、二叉搜索树的中序遍历为递增数组，直接遍历求n-k
        2、递归途中不断缩小k的值进行计算
        :param root:
        :param k:
        :return:
        '''
        num = []
        def recur(root):
            if not root:
                return
            recur(root.left)
            num.append(root.val)
            recur(root.right)
        # recur(root)
        # return num[len(num)-k]

        '''
        时间/空间复杂度 最坏O(n)
        树呈现链表的形式
        '''
        self.k = k
        def recur2(root):
            if not root:
                return
            recur2(root.left)
            if self.k==0:
                return
            self.k-=1
            if self.k==0:
                self.res = root.val
            recur2(root.right)

        return 

