'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
示例 1：

输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
示例 3：

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]
示例 4：

输入：head = [1], k = 1
输出：[1]
提示：

列表中节点的数量在范围 sz 内
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 翻转一个子链表，并且返回新的头与尾
        def tail_insert_reverse(head, tail):
            # 记录当前节点的后续节点，并且把尾节点之后置为None单独分隔开
            pre = tail.next
            tail.next = None
            # 尾插法翻转链表
            while head!=tail:
                # 头尾节点相等时代表终止
                # 记录尾插法之后的节点
                tail_nxt = tail.next
                # 记录当前节点之后的节点
                head_nxt = head.next
                # 尾插
                tail.next = head
                head.next = tail_nxt
                head = head_nxt
            # 尾节点变头节点，找到当前片段的尾部节点
            cur = tail
            while cur.next:
                cur = cur.next
            # 找到尾节点之后，再链接之前的节点部分
            cur.next = pre
            return tail, cur
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur:
            # 记录要反转片段首节点之前的一个节点
            pre_start = cur
            start = cur.next
            #长度是否为k，如果不为k不用翻转，直接返回
            for i in range(k):
                cur = cur.next
                if not cur:
                    return dummy.next
            end = cur
            start, end = tail_insert_reverse(start, end)
            pre_start.next = start
            cur = end
        return dummy.next