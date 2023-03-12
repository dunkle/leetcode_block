# 1008. Construct Binary Search Tree from Preorder Traversal

![image-20200420174550863](../../../.assert/image-20200420174550863.png)

给定一个先序遍历的二分搜索树构造原树。

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        r = 1
        while r < len(preorder) and preorder[r] < preorder[0]:
            r += 1
        root.left = self.bstFromPreorder(preorder[1:r])
        root.right = self.bstFromPreorder(preorder[r:])
        return root
            
~~~

