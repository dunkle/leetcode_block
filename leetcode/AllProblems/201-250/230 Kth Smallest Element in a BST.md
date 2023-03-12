# 230. Kth Smallest Element in a BST

![image-20200403175239980](../../.assert/image-20200403175239980.png)

给定一个二叉搜索树，找到第k小的值

## 中序遍历

二叉搜索树的中序遍历的结果是一个顺序数组，因此可以通过中序遍历找到第K个数

**递归版本**

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def helper(node, result):
            if node == None:
                return None
            
            l = helper(node.left, result)
            if l is not None:
                return l
            result.append(node.val)
            if len(result) == k:
                return result
            r = helper(node.right, result)
            if r is not None:
                return r
            return None
        
        
        return helper(root, [])[-1]
~~~

**迭代版本**

~~~python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        n = k
        k = 0
        while True:
            
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            k = k + 1
            if k == n:
                return node.val
            root = node.right
~~~

