'''
从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。
示例：
给定如下二叉树

        2
       / \
      1   3
返回：

[
   [2,1,3],
   [2,3,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bst-sequences-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def BSTSequences(self, root):
        res = []
        if root is None:return [[]]
        temp = [root.val]
        def help(root, queue, path):
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            if len(queue) == 0:
                res.append(temp + path)
            # 此处设置一个que队列，用来存储所有的子节点
            for i in range(len(queue)):
                # 从所有的子孩子中选出一个，其他的子孩子没被选择，往下递归
                # 从队列中选出的节点，可以是任意一个节点的左右孩子。
                next_root = queue[i]
                next_queue = queue[:i] + queue[i+1:]
                help(next_root, next_queue, path + [next_root.val])

        help(root, [], [])
        return res


