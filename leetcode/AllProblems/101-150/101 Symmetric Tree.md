# 101. Symmetric Tree

判断两个二叉树是否为对称的

![image-20200329130605655](../.assert/image-20200329130605655.png)

~~~python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                l = helper(node1.left, node2.right)
                r = helper(node1.right, node2.left)
                return l and r
            return False
        
        if root is None:
            return True
        return helper(root.left, root.right)
~~~

