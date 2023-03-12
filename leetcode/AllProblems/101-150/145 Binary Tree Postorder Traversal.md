需要记录每个节点是否访问过，如果没访问过，就迭代右子树，否则，说明左右子树都跌带过，输出。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        p = root
        ret = []
        while p or stack:
            while p:
                stack.append([p, 0])
                p = p.left
            if stack:
                top = stack[-1]
                if top[1] == 0:
                    top[1] = 1
                    p = top[0].right
                else:
                    ret.append(top[0].val)
                    stack.pop()
                    p = None
        return ret
```

