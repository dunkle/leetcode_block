# 148. Sort List

![image-20200426150657699](../../../.assert/image-20200426150657699.png)

给定一个链表，在时间复杂度为$O(nlogn)$和空间复杂度为O(1)的情况下进行排序。

首先使用两个指针slow,fast找到中间节点，对链表分成两部分排序，然后对其进行归并排序。

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        l, r = head, slow.next
        slow.next = None
        l = self.sortList(l)
        r = self.sortList(r)
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = ListNode(0)
        tail = dummy
        while l and r:
            if l.val < r.val :
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        while l:
            tail.next = l
            l = l.next
            tail = tail.next
        while r:
            tail.next = r
            r = r.next
            tail = tail.next
        return dummy.next
~~~

注：在寻找中间节点的时候，要让fast=head.next，因为考虑如下这种情况[1,2]，此时fast为None，slow为2，head为1，l指向head，r指向slow，此时对l做sort会永远递归下去，所以先让fast向下移动一个节点用于处理长度为2的链表这种特殊情况。