'''
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        归并排序法
        要求使用O(nlgn)的时间复杂度，因此必定会要求使用二分的思想
        此处把链表拆分成两段，再利用合并两个链表的思路
        拆分使用快慢指针，一个走一步一个走两步
        :param head:
        :return:
        '''
        def mergenode(node1, node2):
            # print(node1)
            # print(node2)
            start1 = node1
            start2 = node2
            pre = ListNode(-1)
            cur = pre
            while start1 and start2:
                if start1.val<start2.val:
                    cur.next = start1
                    start1 = start1.next
                else:
                    cur.next = start2
                    start2 = start2.next
                cur =cur.next
            if start1:
                cur.next = start1
            else:
                cur.next = start2
            return pre.next
        def spiltnode(node):
            if not node or not node.next:
                return node
            # 当只有两个节点时，一个在前一个在后进行判断
            slow = node
            fast = node.next
            # 此处采用fast.next 判断该节点不为空，那么即使指针移到 fast.next.next为空也不影响
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            # 找到中间节点之后分割为前后两个链表

            # 先记录后链表 slow.next
            backward = slow.next
            # 记录前链表时需要把中间断开
            slow.next = None
            foward = node
            # print(foward)
            # print(backward)
            # 获得前后链表之后再合并两个链表
            return mergenode(spiltnode(foward), spiltnode(backward))
        return spiltnode(head)
a = Solution()
nodes = ListNode(-1)
cur =nodes
arr = [2,4,2,1,3]
for i in arr:
    node =ListNode(i)
    cur.next = node
    cur = cur.next

def printnode(nodes):
    cur = nodes
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


now = a.sortList(nodes.next)
printnode(now)


