# 102. Binary Tree Level Order Traversal

![image-20200406163935816](../../.assert/image-20200406163935816.png)

返回二叉树层序遍历的list

~~~python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            result.append([n.val for n in queue])
            current_queue = []
            for n in queue:
                if n.left:
                    current_queue.append(n.left)
                if n.right:
                    current_queue.append(n.right)
            queue = current_queue
        return result
~~~

