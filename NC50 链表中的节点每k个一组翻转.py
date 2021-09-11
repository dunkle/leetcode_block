class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class Solution:
    def reverseKGroup(self, head, k):
        flag = 1
        cur = head
        dummy = ListNode(-1)
        dummy.next = None
        tail = dummy.next
        pre = dummy
        while cur:
            if (flag%k)!=0:
                # 记录当前翻转部分的尾节点
                if flag%k==1:
                    tail = cur

                # 记录当前cur节点之后的节点
                tmphead = cur.next
                # 断开当前节点
                cur.next = None

                # 当前节点头插到新的链表做翻转
                # 头插，先记录当前头节点之后的节点，cur节点加入 头节点之后的节点
                tmp = pre.next
                pre.next = cur
                # 当前节点之后的节点连接 头插断开的后半部分
                cur.next = tmp

                # cur 节点继续往前
                cur = tmphead
            else:

                pre = tmphead
