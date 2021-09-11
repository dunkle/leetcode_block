class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        if n==0:
            return 0
        l,r = 0, n-1
        # 添加一个标志，判断原始数组是否存在元素
        start = None
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                # start 最终会停留在等于该元素的位置
                start = mid
                # 如果找到，则递归往左边继续找，收缩左边界
                r = mid-1
        if start==None:
            return 0

        l,r = 0, n-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                # end 最终会停留在目标元素位置上
                end = mid
                # 如果找到，则递归往右边继续找，收缩右边界
                l = mid+1
        # print(end)
        return end-start+1

a = Solution()
nums = [1,2,3,3,3,4,5]
target = 3
nums = [1]
target = 1
res = a.search(nums, target)
print(res)