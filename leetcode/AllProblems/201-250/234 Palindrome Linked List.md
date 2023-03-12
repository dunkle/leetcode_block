# 234. Palindrome Linked List

![image-20200402152404962](../../.assert/image-20200402152404962.png)

给定一个一个链表，判断链表是否是回文

首先用两个指针，一个遍历步长为1，一个遍历步长为2，当后者遍历到尾节点时，前者会处于中间的位置，在遍历的时候同时用一个指针将前半个链表反转。然后比较反转链表和1步长的节点是否相同。

~~~python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
~~~

