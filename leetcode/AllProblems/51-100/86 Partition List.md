![image-20201008160841708](../../../.assert/image-20201008160841708.png)

给定一个链表，将大于x的放到前面小于x的放到后面并不改变之前链表的相对位置。

为了保证相对位置，将等于x的Node划分到大于的部分

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1, h2 = ListNode(0), ListNode(0)
        p1, p2 = h1, h2
        while head != None:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = h2.next
        h2.next, p2.next = None, None
        return h1.next
~~~

