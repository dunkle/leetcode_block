![image-20210208135124616](../../../.assert/image-20210208135124616.png)

给定一个完全二叉树，将每个节点的next指针指向其右边的元素。

## 解法

层序遍历每层节点，设置其子节点的next指针

```
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head, cur = root, root
        while cur and cur.left:
            head = cur
            while cur:
                cur.left.next = cur.right
                if cur.next != None:
                    cur.right.next = cur.next.left
                cur = cur.next
            cur = head.left
        return root
```

