![image-20201008163253125](../../../.assert/image-20201008163253125.png)

反转给定范围的链表。

首先定位到前一个Node，然后反转之后n-m+1个节点。

~~~pyhton
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        for _ in range(m-1):
            start = start.next
            
        tail = None
        p = start.next
        start.next = None
        for _ in range(n-m+1):
            t = p.next
            p.next = start.next
            start.next = p
            if tail == None:
                tail = p
            p = t
        tail.next = p
        return dummy.next
            
        
~~~

