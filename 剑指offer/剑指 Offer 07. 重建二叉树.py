class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, preorder, inorder):
        def recur(root, left, right):
            if left > right: return                               # 递归终止
            # 先序遍历的第一个节点为根节点，构建新节点存入
            node = TreeNode(preorder[root])                       # 建立根节点

            # 在中序的dict里找 根节点 在中序遍历的索引，索引左侧是左子树，右侧是右子树
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树

            # root+1 代表了左子树的根节点，left->i-1代表所有左子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            #
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        # 先构建中序遍历的字典，方便查找
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        # 只传入 下标位置 进行递归
        return recur(0, 0, len(inorder) - 1)

    def buildTree1(self, preorder, inorder):
        def recur(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left>preorder_right:
                return
            preorder_root = TreeNode(preorder[preorder_left])
            inorder_index = dic[preorder[preorder_left]]
            # 计算一下左子树的长度
            lenth_left_tree = inorder_index-inorder_left
            # 左子树递归，先序遍历的数组 从 当前根节点+1位置 ，到，根节点+左子树长度
            preorder_root.left = recur(preorder_left+1, preorder_left+lenth_left_tree,
                                       inorder_left, inorder_index-1)

            # 右子树的根节点，从先序里找，Root Left Right,
            # root+1是左子树的根节点，需要知道左子树的长度， root+1 + Lenth(左子树长度)就是右子树根节点
            preorder_root.right = recur(preorder_left+1+lenth_left_tree,
                                        preorder_right, inorder_index+1, inorder_right)
            # 返回当前构造节点的根节点
            return preorder_root

        dic, preorder = {}, preorder
        # 先构建中序遍历的字典，方便查找
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        # 只传入 下标位置 进行递归
        return recur(0, len(preorder)-1, 0,len(inorder) - 1)


