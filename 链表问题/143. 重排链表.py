'''
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        重排链表，分三步
        1、找链表中点，拆分为两个链表
        2、链表前部分 顺序排， 后部分 逆序排
        3、合并两个链表
        '''
        if not head or not head.next:
            return head
        def split(head):
            slow = head
            fast = head
            # 快慢指针判断界限，当fast.next.next 有值， slow最终是停在中间节点上
            # 1 2 3 4
            # 第一次走 1 2 3 4
                       #S F 并且无法走第二次
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            # 后部链表是以slow停留的链表之后
            tmp = slow.next
            slow.next = None
            return head, tmp
        def reverse(node):
            pre = ListNode(-1)
            pre.next = None
            while node:
                tmp = pre.next
                pre.next = node
                node = node.next
                pre.next.next = tmp
            return pre.next
        def merge(node1, node2):
            # print(node1)
            # print(node2)
            cur = node1
            # print(cur)
            # 合并链表 就是 以一个链表为主链表，下面链表插入到该链表
            while cur and node2:
                tmp1 = cur.next
                cur.next = node2
                node2 = node2.next
                cur.next.next = tmp1
                cur = tmp1
            return node1

        foward, backward = split(head)
        backwardreverse = reverse(backward)
        mergenode = merge(foward, backwardreverse)
        return mergenode




