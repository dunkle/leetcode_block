![image-20210224205856001](../../../.assert/image-20210224205856001.png)

头插法，新建一个节点进行排序

```python
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummpy = ListNode(0)
        q = dummpy
        p = head
        while p:
            q = dummpy
            np = p.next
            while q:
                if q.next is None or q.next.val > p.val:
                    p.next = q.next
                    q.next = p
                    break
                else:
                    q = q.next
            p = np
        return dummpy.next
```

