'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution2:
    def partion(self, nums, l, r):
        # print("shuzu", nums)
        pivot = nums[l]
        while l<r:
            #当以最左边元素作为pivot时，需要从右边开始找最小的 可以覆盖pivot上的值
            while l<r and nums[r]>pivot:
                r-=1
            nums[l] = nums[r]
            while l<r and nums[l]<=pivot:
                l+=1
            nums[r] = nums[l]
        nums[l] = pivot
        return l

    def findKthLargest(self, nums, k):
        index  =self.partion(nums,0, len(nums)-1)
        # print(index)
        if index+1<k:
            knum = self.findKthLargest(nums[index+1:], k-index-1)
        elif index+1>k:
            knum = self.findKthLargest(nums[:index], k)
        else:
            # print("k", nums[index])
            knum =  nums[index]
        return knum
# a = Solution()
a = Solution2()
nums = [3,2,1,5,6,4]
k = 2
#此处是 最大的第k个数，因此需要用总长度减去k
f= a.findKthLargest(nums, len(nums)-k+1)
print(nums)
print(f)