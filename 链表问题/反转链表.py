class Solution:
    def reverseList(self, head):
        '''
        头插法-》》链表翻转分为四步
        1、先记住要断开结点（当前节点）的下一个节点 nxt = cur.next
        2、断开结点，断开的节点 需要头插到新链表的 头部 cur.next = pre
        3、更新 新链表的头节点
        4、更新 当前节点
        :param head:
        :return:
        '''
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    def reverseList1(self, head):
        '''
        尾插法-》》链表翻转分为四步
        1、找到不为None的尾节点tail
        2、指针head一直从头往后获得节点，并且插在tail尾节点之后
        3、终止条件是head 和tail相等
        4、插入之前需要保存tailnxt 和headnxt
        5、更新head节点
        '''
        if not head:
            return head
        cur = head
        while cur.next:
            cur =  cur.next
        head, tail = head, cur
        while head!=tail:
            tail_nex = tail.next
            head_nxt = head.next
            tail.next = head
            head.next = tail_nex
            head = head_nxt
        return tail