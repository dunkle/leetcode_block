'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
 

提示：

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def __init__(self):
        self.num = 0
    def countSmaller(self, nums):
        pass
    def mergesort(self, nums):
        def partition(nums):
            n = len(nums)
            if n<=1:
                return nums
            mid = n//2
            left = partition(nums[0:mid])
            right = partition(nums[mid:])
            return merge(left, right)
        def merge(left, right):
            tmp = []
            m = len(left)
            n = len(right)
            i, j= 0, 0
            while i<m and j<n:
                if left[i]<=right[j]:
                    tmp.append(left[i])
                    i+=1
                else:
                    self.num = self.num+1
                    tmp.append(right[j])
                    j+=1

            tmp.extend(left[i:])
            tmp.extend(right[j:])
            self.num= self.num + (m-i)*n
            return tmp
        return partition(nums), self.num

a = Solution()
arr = [7,5,6,4]
res, count = a.mergesort(arr)
print(res)
print(count)