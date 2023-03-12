# 328. Odd Even Linked List

![image-20200406163059250](../../.assert/image-20200406163059250.png)

将位于偶数位置的元素移到奇数位置之后，元素的顺序不可改变

## 插入排序

用一个指针记录偶数位置的头，一个指针记录下一个奇数位置，将奇数指针的值不断与偶数指针的值交换。

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        even = head.next
        odd = even.next
        while odd and even:
            tmp = even
            while tmp != odd:
                tmp.val, odd.val = odd.val, tmp.val
                tmp = tmp.next
            even = even.next
            odd = odd.next.next if odd.next else odd.next
        return head
~~~

## 构造链表

三个指针：

1. evenhead，记录偶数位置元素链表的头
2. even，记录下一个偶数链表的尾部
3. odd，记录奇数链表的尾部

将链表切分成奇数偶数两个链表之后将奇数链表的尾指针指向偶数链表的头指针即可。

![Illustration of odd even linked list](../../.assert/328_Odd_Even.svg)

~~~python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        evenhead = head.next
        even = evenhead
        odd = head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head
~~~

