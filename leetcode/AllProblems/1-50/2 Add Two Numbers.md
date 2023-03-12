# 2. Add Two Numbers

给定两个整数,以逆序存放在链表中,求这两个整数的和的链表.

直接从最低位开始相加即可.

注意divmod的返回值是(除数,余数)

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        p = head
        
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
                
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            carry, val = divmod(v1+v2+carry, 10)
            p.next = ListNode(val)
            p = p.next
            
        return head.next
~~~

