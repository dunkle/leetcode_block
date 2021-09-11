'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def pathSum(self, root, targetSum):
        '''
        1、需要考虑值为负数的情况，因此无需判断值是否大于或者小于targetSum 只需要判断是否相等
        2、因为是从根节点到叶子节点的一条完整路径，即使出现累加到目前状态的值相等时，也需要继续判断直到叶子节点
        3、在添加esults 时需要 进行copy操作
        :param root:
        :param targetSum:
        :return:
        '''
        results = []
        if not root:
            return results
        def recur(root, targetSum, nowresults):
            nowresults.append(root.val)
            if root.left:
                recur(root.left, targetSum-root.val, nowresults)
            # nowresults.pop()
            if root.right:
                recur(root.right, targetSum-root.val, nowresults)
            nowresults.pop()
            if not root.left and not root.right and root.val==targetSum:
                nowresults.append(root.val)
                results.append(nowresults.copy())
                nowresults.pop()
            return
        recur(root, targetSum, [])
        return results