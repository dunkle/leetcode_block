# 108. Convert Sorted Array to Binary Search Tree

~~~python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        i = len(nums) // 2
        n = TreeNode(nums[i])
        n.left = self.sortedArrayToBST(nums[:i])
        n.right = self.sortedArrayToBST(nums[i+1:])
        return n
~~~

~~~python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(nodes):
            if len(nodes) == 0:
                return None
            if len(nodes) == 1:
                return TreeNode(nodes[0])
            i = len(nodes) // 2
            n = TreeNode(nodes[i])
            n.left = self.sortedArrayToBST(nodes[:i])
            n.right = self.sortedArrayToBST(nodes[i+1:])
            return n
        
        return helper(nums)
~~~

