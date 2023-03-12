给定一个链表，删除其中所有包含重复值的元素。

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 创建一个链表头
        dummpy = ListNode(-1)
		# tail 表示前一个节点
        tail = dummpy
        tail.next = head
        # p指向当前节点
        p = head
        while p:
            # 如果p是重复值
            if p.next and p.val == p.next.val:
                # 找到重复值的最后一个节点
                while p and p.next and p.val == p.next.val:
                    p = p.next
                # 指向重复值的下一个节点，下一个节点可能是重复值
                tail.next = p.next
            # 如果p不是重复值，则直接移动尾节点
            else:
                tail = tail.next
            p = p.next
        return dummpy.next
~~~

