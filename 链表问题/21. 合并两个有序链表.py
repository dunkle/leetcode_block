'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        # 设置一个 哑节点 ，这样可以不用考虑头节点的影响
        dummy.next = head
        start = dummy
        # 从next节点开始，头节点是亚节点
        while start.next and start.next.next:
            # 如果next 节点 与 与 next.next 节点值一致
            # 1 1 2 3 3 4 5
            if start.next.val==start.next.next.val:
                # 设置一个 pivot 往下搜索，如果与next节点值一致，往下走直到走到不一致
                pivot = start.next.val
                while start.next and start.next.val==pivot:
                    # 让next 接下 next.next
                    start.next = start.next.next
            else:
                start = start.next
        return dummy.next
