class Solution(object):
    def detectCycle(self, head):
        '''
        设链表共有 a+b 个节点，其中 链表头部到链表入口 有 a 个节点（不计链表入口节点）， 链表环 有 b 个节点
        第一次相遇假设， 两指针分别走了 f，s 步
        fast 走的步数是slow步数的 22 倍，即 f = 2s； (1)
        fast 比 slow多走了 n 个环的长度，即 f = s + nb；(2)
        （ 解析： 双指针都走过 a 步，然后在环内绕圈直到重合，重合时 fast 比 slow 多走 环的长度整数倍 ）；
        (1)-(2) -> s=nb -> 再反带回去 f = 2nb

        因此可以推出-》》 第一次相遇时慢指针已经走了nb步，慢指针再走 a步就是入口处的节点
        因此把快指针重新置为头部，两者 第二次相遇就是入口处节点

        走a+nb步一定是在环入口
        :param head:
        :return:
        '''
        fast, slow = head, head
        while True:
            # 第一种结果： fast 指针走过链表末端，说明链表无环，直接返回 null；
            if not (fast and fast.next): return

            fast, slow = fast.next.next, slow.next
            # 当fast == slow时， 两指针在环中 第一次相遇 。
            if fast == slow: break
        # 把快指针重新置为头部，两者 第二次相遇就是入口处节点，再走a步
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
