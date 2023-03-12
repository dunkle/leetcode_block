# 876. Middle of the Linked List

![image-20200408172725081](../../.assert/image-20200408172725081.png)

给定一个链表，求链表的中间节点

## 多次遍历

第一次遍历求出数组的长度，然后在遍历一次到中间节点。

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head: return head
        i,curr = 0, head
        while curr:
            i,curr = i+1, curr.next
        
        mid,i,curr = i // 2, 0, head
        
        while curr:
            if i == mid: return curr
            i, curr = i+1, curr.next
~~~

~~~go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    p, l := head, 0
    for p != nil {
        p, l = p.Next, l+1
    }
    mid := l / 2
    p = head
    for l := 0;l < mid;l++ {
        p = p.Next
    }
    return p
}
~~~

## 一次遍历

设置两个指针，一个一次跳两个节点，一个跳一个节点，分别为fast和slow

~~~python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
~~~

~~~go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    slow, fast := head, head
    for ;fast != nil && fast.Next != nil;{
        fast = fast.Next.Next
        slow = slow.Next
    }
    return slow
}
~~~

