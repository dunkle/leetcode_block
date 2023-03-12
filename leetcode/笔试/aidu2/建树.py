#coding=utf-8
import sys
#str = input()
#print(str)

'''
1. a = [0,1,2,3,4,5], 定义一个二叉树节点类，写一个二叉树的建树过程
       0
      / \
     1  2
    /\   /
  3 4 5

2. 求该树深度
3. 前序遍历打印该树
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildtree(a):
    if len(a)==0:
        return None
    head = Node(a[0])
    que = []
    que.append(head)
    n = len(a)
    i = 1
    while que:
        now = que.pop(0)
        #         print(now.val)
        if i<n:
            now.left = Node(a[i])
            que.append(now.left)
            i+=1
        if i<n:
            now.right = Node(a[i])
            que.append(now.right)
            i+=1
        if i>=n:
            break
    return head

def callenth(head):
    if not head:
        return 0
    left = callenth(head.left)+1
    right = callenth(head.right)+1
    return max(left, right)


def bianli(head):
    # Root L r
    if not head:
        return
    print(head.val)
    bianli(head.left)
    bianli(head.right)

a = [0,1,2,3,4,5]
nodetree = buildtree(a)
res = callenth(nodetree)
bianli(nodetree)
print(res)


