'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 
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

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode):
        '''
        1、使用快慢指针找到中点（因为取head容易被卡），取到划分值val
        2、使用6个变量，分别表示小于部分的头(真正head的前一个节点)和尾，等于部分的头和尾，大于部分的头和尾
        3、快排partition过程
        对小于部分和大于部分递归
        合并结果，等于部分一定不为空，注意小于部分可能为空

        作者：chu-yang-er-shi-er
        链接：https://leetcode-cn.com/problems/sort-list/solution/lian-biao-pai-xu-kuai-pai-ji-gui-bing-by-m70f/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        :param head:
        :return:
        '''
        def quicksort(head):
            if not head:
                return head
            pivot = head.val
            dummy1 = ListNode(-1)
            dummy2 = ListNode(-1)
            cur1 = dummy1
            cur2 = dummy2
            while head:
                if head.val<pivot:
                    cur1.next = head
                    cur1 = cur1.next
                else:
                    cur2.next = head
                    cur2 = cur2.next
                head = head.next
            cur1.next = cur2.next = None

            beforenode = quicksort(dummy1)
            afternode = quicksort(dummy2)
            printnode(beforenode)
            printnode(afternode)
            beforelast = beforenode
            while beforelast.next:
                beforelast = beforelast.next
            beforelast.next = afternode
            while afternode:
                afternode = afternode.next
            afternode.next = None
            return beforenode
        return quicksort(head)

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


now = a.sortList(nodes)
printnode(now)


