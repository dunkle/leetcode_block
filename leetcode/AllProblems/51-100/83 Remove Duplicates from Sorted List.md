![image-20201006215600280](../../../.assert/image-20201006215600280.png)

去除排序链表中的重复元素

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            if p.val == p.next.val:
                t = p.next
                p.next = t.next
                t.next = None
            else:
                p = p.next
        return head
~~~

