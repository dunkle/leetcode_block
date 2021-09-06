class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        '''
        1、计算链表长度
        2、模链表长取余
        3、取倒数n-k个
        4、前后调换
        :return:
        '''
        # 计算链表长度
        cur = head
        flag = 0
        while cur:
            flag+=1
            cur = cur.next
        # 链表长度为0或者1 直接返回
        if flag<2:
            return head
        # 每转flag次代表链表不动
        k = k%flag
        # 为0代表链表不动
        if k==0:
            return head
        # print(flag)
        # 转k次相当于把 链表倒数n-k个节点和前面节点调换
        cur = head
        # 取倒数n-k个
        k = flag-k
        flag = 0
        while cur:
            flag+=1
            if flag==k:
                break
            cur = cur.next
        # 前后调换
        newhead = cur.next
        cur.next = None
        cur = newhead
        while cur.next:
            cur = cur.next
        cur.next = head
        return newhead