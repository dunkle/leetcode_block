class Solution:
    def reverseList(self, head):
        '''
        链表翻转分为四步
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