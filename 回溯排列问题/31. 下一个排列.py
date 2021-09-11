'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
        Do not return anything, modify nums in-place instead.
        1、从后往前找第一个(i,j)是升序的 nums[i] > nums[j]
        2、从后往前找第一个大于nums[i]的数进行交换, nums[k]>nums[i]
        3、交换之后，从第i个位置起始处往后 仍然是降序排列的数组
        4、以升序排列重排数组i之后的数，两数交换即可
        """
        n = len(nums)
        if n<2:
            return nums
        # 满足第一步，找到i，j
        i,j = n-2, n-1
        while i>=0 and nums[j]<=nums[i]:
            i-=1
            j-=1
        # i一直往前，当等于-1代表了整个序列都是递减序列，也就是处于最大值状态
        # 因此直接返回逆序数组就行
        if i==-1:
            nums.reverse()
            # return nums
        else:
            # 满足第二步找到k并且交换
            j = n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
            # 满足第3、4步骤
            start = i+1
            end = n-1
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
            # return nums

a = Solution()
nums = [1,2,3]
nums = [3,2,1]
nums = [1,1,5]
# nums = [1,3,2]
a.nextPermutation(nums)
print(nums)