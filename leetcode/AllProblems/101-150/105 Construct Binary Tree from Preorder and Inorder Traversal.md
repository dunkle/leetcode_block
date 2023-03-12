# 105. Construct Binary Tree from Preorder and Inorder Traversal

![image-20200413013331596](E:\OneDrive\笔记\.assert\image-20200413013331596.png)

给定中序和先序遍历的二叉树，还原二叉树

~~~python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = preorder[0]
        root_index = inorder.index(root)
        
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        root = TreeNode(root)
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
~~~

