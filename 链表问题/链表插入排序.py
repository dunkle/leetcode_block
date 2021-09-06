# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 链表为空直接返回
        if not head:
            return
        # 设置哑节点
        dummy = ListNode(-1)
        dummy.next = head
        # 设置已经排好序的尾节点
        lastsorted = head

        #链表的当前节点，当cur指向空代表排序完
        cur = head.next
        while cur:
            if cur.val>=lastsorted.val:
                # 当前节点都比排好序的尾节点大，直接插入在尾节点
                lastsorted = lastsorted.next
            else:
                # 比尾节点小，那么从头开始找
                # 需要设置一个开始查找节点，将cur节点，和当前节点的下一个节点比较，因为要插入在前面
                start_sorted = dummy
                while start_sorted.next.val<=cur.val:
                    # 直到找到下一个节点比当前节点大
                    start_sorted = start_sorted.next
                # 链表插入，先保存cur的下一个节点，以及查找到的节点之后的节点
                lastsorted.next = cur.next #** 关键点，把尾部节点直接连接cur的next标记
                start_sorted_nxt = start_sorted.next
                # 插入
                start_sorted.next = cur
                #再接上之后拍好序的节点
                cur.next = start_sorted_nxt
            # 更新当前节点
            cur = lastsorted.next
        return dummy.next

