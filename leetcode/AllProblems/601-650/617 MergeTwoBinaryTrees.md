# 617 Merge Two Binary Tree

## 自己的解法



~~~python
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        return self._merge(root1=t1, root2=t2)
        
    def _merge(self, root1, root2):

        if root1 is None and root2 is not None:
            return root2
        
        if root1 is not None and root2 is None:
            return root1

        if root1 is not None and root2 is not None:
            root = TreeNode(root1.val + root2.val)
            root.left = self._merge(root1.left, root2.left)
            root.right = self._merge(root1.right, root2.right)
            return root
        return None
~~~

## 优化1

1. 将递归写道一个函数里
2. 两个节点均为空的数量远小于不为空的概率，因此优先判断二者都为空的概率，使判断if的次数尽可能的少

~~~python
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        if not t1 and t2:
            return t2
        
        if t1 and not t2:
            return t1

        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root
~~~

