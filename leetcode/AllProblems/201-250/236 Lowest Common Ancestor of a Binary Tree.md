# 236. Lowest Common Ancestor of a Binary Tree

![image-20200418164407654](../../../.assert/image-20200418164407654.png)

给定一个二叉树和两个节点，找到二者的最近公共祖先

## 记录路径

记录从根节点到两个节点的路径，找到不同的那个位置。

~~~python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(path, n, p):
            if n == None:
                return None
            if n.val == p.val:
                return path + [n]
            p1 = get_path(path + [n], n.left, p)
            if p1 != None:
                return p1
            p2 = get_path(path+[n], n.right, p)
            return p2
        
        p_path = get_path([], root, p)
        q_path = get_path([], root, q)
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i].val == q_path[i].val:
            i += 1
        return p_path[i-1]
~~~

## DFS

对于任意一个节点：

- 如果在其左子树和右子树找到p和q，那么该节点为公共祖先。
- 如果在左子树或右子树找到p或q，那么公共祖先在之前的节点。
- 如果左右子树都没找到p和q，那么公共祖先不在当前的子树上

~~~python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        if p.val == root.val:
            return p
        
        if q.val == root.val:
            return q
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right
        
        if not right:
            return left
        
        return root
        
~~~

