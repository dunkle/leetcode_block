# 206 Reverse Linked List

## 迭代算法

~~~python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        nex = head.next
        cur = p = head
        
        while cur:
            cur = nex.next
            nex.next = p
            p = nex
            nex = cur
        head.next = None
        
        return p
~~~

## 递归算法

1. end的next要设置为None，否则原链表的第一个Node会和第二个节点构成环
2. 设置两个node，一个记录头，一个记录尾

~~~python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return head
        def parent(node, end):
            if node.next is None:
                end = node
                return node, end
            p, end = parent(node.next, end)
            end.next = node
            end = node
            end.next = None
            return p, end
        
        p, e = parent(head, None)
        return p
~~~

