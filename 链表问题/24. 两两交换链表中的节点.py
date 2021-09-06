class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        cur = pre
        while cur.next and cur.next.next:
            tmp0 = cur.next.next.next
            tmp1 = cur.next.next
            cur.next = cur.next.next


