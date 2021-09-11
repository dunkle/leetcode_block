'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        if not root:
            return result
        queue = [root, "*"]
        level = 0
        tmp = [root]
        while queue:
            node = queue.popleft()
            if node=='*':
                result.append(tmp)
                tmp = []
                continue
            if level%2==0:
                if node.left:
                    tmp.append(node.left)
                    queue.append(node.left)
                if node.right:
                    tmp.append(node.right)
                    queue.append(node.right)
                level+=1
            elif level%2==1:
                queue.append(node.right)
                queue.append(node.left)
            result.append(tmp)
