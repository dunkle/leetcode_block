'''
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
删除完毕后，请你返回最终结果链表的头节点。
你可以返回任何满足题目要求的答案。
（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）
示例 1：

输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
示例 2：

输入：head = [1,2,3,-3,4]
输出：[1,2,4]
示例 3：

输入：head = [1,2,3,-3,-2]
输出：[1]

提示：

给你的链表中可能有 1 到 1000 个节点。
对于链表中的每个节点，节点的值：-1000 <= node.val <= 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        dictmap = {}
        tmp = 0
        # 依次求每个节点的前缀和
        # 后面的节点如果和之前的节点前缀和相同，会覆盖dict对应value值（之前的节点值）
        while cur:
            tmp +=cur.val
            dictmap[tmp] = cur
            cur = cur.next

        cur = dummy
        tmp = 0
        # # 再次从头开始求前缀和
        while cur:
            tmp += cur.val
            # 将当前位置的指向的节点指向 相同前缀和的节点，代表这两段是一样的
            cur.next = dictmap[tmp].next
            cur = cur.next
        return dummy.next