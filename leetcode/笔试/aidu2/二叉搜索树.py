# 二叉搜索树 left< Root< Right
# 输入一棵树，判断是否为平衡二叉树,
#     6
#   5 10
#4 9
class Solution:
    def isValidBST(self, root):
        return self.dg(root,float('-inf'),float('inf'))
    def dg(self,root,min_v,max_v):
        # 参数：root：当前节点，min_v：允许最小值（下界），max_v：允许最大值（上界）

        if root == None: # 如果当前节点为空，证明已经递归到叶子节点，返回True
            return True

        if root.val < max_v and root.val > min_v : # 如果当前节点值符合规定，继续进行之后的递归
            pass
        else: # 如果不符合规定，之间返回 False
            return False

        if self.dg(root.left,min_v,root.val) == False: # 对左子树进行递归，此时最大值应该为当前节点值
            return False
        if self.dg(root.right,root.val,max_v) == False:# 对右子树进行递归，此时最小值应该为当前节点值
            return False

        return True # 如果成功避开所有坑，这个当前节点下的子树是一个二叉搜索树
