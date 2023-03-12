# 104 Maximum Depth of Binary Tree

## 自己的解法

~~~python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
~~~

## 优化1

当root的左子树或右子树为空时直接赋值，减少函数调用

~~~python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0
        return max(left, right) + 1
~~~

## 优化2

使用list模拟栈，层序遍历二叉树得到深度。

这里使用了一个技巧，将深度同时push到队列中，因此可以从队列中取出当前节点的深度。

~~~python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        queue = [(root ,1)]
        depth = 0
        while queue:
            node, d = queue.pop()
            depth = max(depth, d)
            if node.left:
                queue.append((node.left, d+1))
            if node.right:
                queue.append((node.right, d+1))
        return depth
~~~

