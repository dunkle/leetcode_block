# 21. Merge Two Sorted Lists

在最后直接link剩下的节点即可，不必遍历

~~~python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        end = result
        
        while l1 and l2:
            if l1.val > l2.val:
                end.next = l2
                l2 = l2.next
                end = end.next
            else:
                end.next = l1
                l1 = l1.next
                end = end.next
        if l1:
            end.next = l1
        elif l2:
            end.next = l2
        # while l1:
        #     end.next = l1
        #     end = end.next
        #     l1 = l1.next
        # while l2:
        #     end.next = l2
        #     end = end.next
        #     l2 = l2.next
        return result.next
~~~

## 递归

用栈来存放本次选择的节点

~~~python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
~~~



