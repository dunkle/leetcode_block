# Definition for a binary tree node.
'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        # 记录结果
        self.res = []
        # 暂存一条路径
        self.tmp = []
        def recur(root, num):
            if not root:
                return
            # 加上当前节点值
            num = num+root.val
            self.tmp.append(root.val)
            # 加上该节点值之后 等于target 并且 当前节点为叶子节点，添加进res结果
            if num==sum and not root.left and not root.right:
                self.res.append(self.tmp.copy())
                # print(self.tmp)
                # 需要将当前结果最后一个节点弹出
                self.tmp.pop()
                # print(self.tmp)
                return
            # 路径节点值可能为正也可能为负，因此需要递归每一条路径
            recur(root.left, num)
            recur(root.right, num)
            # 递归结束需要将结果弹出，表示这条路径都不存在，弹出当前节点
            self.tmp.pop()
            return
        recur(root, 0)
        return self.res
a = Solution()
# a.pathSum(root, sum)
