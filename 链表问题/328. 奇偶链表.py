'''
328. 奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 可以理解为链表插入问题
        if not head or not head.next:
            return head
        # 直接分别用两个节点保存偶数链 和奇数链
        flag = 1
        # 新节点记录奇偶节点的起始节点
        ou = head.next
        curji = head
        # 奇偶节点移动节点
        curou = ou
        # 当前节点在原链表的位置
        cur = head.next.next
        while cur:
            if flag%2==1:
                # 记录当前节点的后续节点
                tmp = cur.next
                # 分离当前节点
                cur.next = None
                # 奇节点放入奇链表
                curji.next = cur
                # cur当前节点更新
                cur = tmp
                # 奇链表节点往下传递
                curji = curji.next
            else:
                tmp = cur.next
                cur.next = None
                curou.next = cur
                cur = tmp
                curou = curou.next
            flag+=1
        # 把偶节点连接到奇节点之后
        curji.next = ou
        # 偶节点尾部置为none
        curou.next = None
        return head

a = Solution()
nodes = ListNode(-1)
cur =nodes
arr = [1,2,3,4,5]
for i in arr:
    node =ListNode(i)
    cur.next = node
    cur = cur.next
cur = nodes
while cur:
    print(cur.val)
    cur = cur.next
res = a.oddEvenList(nodes)
while res:
    print(res.val)
    res = res.next