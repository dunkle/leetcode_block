class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addInList(self , head1 , head2 ):
        # write code here
        # 翻转链表
        def reverse(head):
            if not head:
                return head
            # 链表翻转
            pre = ListNode(-1)
            # 头插法链表翻转
            while head:
                # 记录下一个节点
                cur = head.next
                # 记录当前头节点的下一个节点
                nxt = pre.next
                # 断开节点
                pre.next = head
                head.next = nxt
                head = cur
            return pre.next
        head1 = reverse(head1)
        head2 = reverse(head2)
        dummy = ListNode(-1)
        newnode = dummy
        flag = 0
        # 由高位向低位相加和
        while head1 and head2:
            addnum = head1.val + head2.val + flag
            flag = addnum//10
            now = addnum%10
            newnode.next = ListNode(now)
            head1 = head1.next
            head2 = head2.next
            newnode = newnode.next
        # 如果仍然包含进位 依次加和 head1 和head2
        while head1:
            addnum = head1.val+ flag
            flag = addnum//10
            now = addnum%10
            newnode.next = ListNode(now)
            head1 = head1.next
            newnode = newnode.next
        while head2:
            addnum = head2.val+ flag
            flag = addnum//10
            now = addnum%10
            newnode.next = ListNode(now)
            head2 = head2.next
            newnode = newnode.next
        # 最后一位进位是否为1
        if flag == 1:
            newnode.next = ListNode(flag)
        # 求和结果进行翻转依次输出
        return reverse(dummy.next)