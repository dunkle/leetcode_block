给定一个非完全二叉树，让每个节点的next指针指向右边的节点。

## 解法

仍然是层序遍历，在父亲节点操作子节点。

prev指针指向的子层链表中最后一个节点。

head指针指向的是子层链表中第一个节点。

```
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev, head = None, None
        node = root
        
        while node:
            if node.left:
                if prev:
                    prev.next = node.left
                prev = node.left
                if not head:
                    head = prev
            
            if node.right:
                if prev:
                    prev.next = node.right
                prev = node.right
                if not head:
                    head = prev
                
            node = node.next
            if not node:
                node = head
                prev, head = None, None
        return root
        
            
```

