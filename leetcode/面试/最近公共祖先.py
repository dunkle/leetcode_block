#coding=utf-8
import sys
#str = input()
#print(str)
'''
满二叉树求LCA
给一棵满二叉树，求任意两个节点的最近公共祖先。树的根节点是1，子节点的值依次递增
1
/ \
2 3
/\ /\
4 5 6 7
样例
Input：4 6
Output：1
'''
a = 4
b = 2
res= []
while True:
    res.append(a)
    if a==0:
        break
    if a%2==0:
        a=a//2
    else:
        a = (a-1)//2
print(res)
while True:
    if b==0:
        break
    if b in res:
        print(b)
        break
    if b%2==0:
        b=b//2
    else:
        b = (b-1)//2


