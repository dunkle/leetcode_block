class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        1、平衡二叉树中序遍历的顺序即为链表的顺序
        2、对一个节点建立前驱和后驱节点
        '''
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            # 先驱节点为None 代表为循环链表的头节点
            if not self.pre:
                self.head = cur
            else:
                # 建立双向链接
                # 先驱节点的右节点为当前节点
                self.pre.right = cur
                # 当前节点的左节点为先驱节点
                cur.left = self.pre
            # 在遍历下一个节点时，需要存一下当前节点，也就是下一个节点的前驱节点
            self.pre = cur
            dfs(cur.right)
        if not root:
            return
        self.head = None
        self.pre = None
        dfs(root)
        # 建立了双向链表之后需要再次建立循环链表，也就是把头尾节点相连
        # 尾节点的右节点时头部节点，当dfs遍历结束之后，节点停在最后一个尾节点处
        self.pre.right = self.head
        self.head.left = self.pre
        return self.head