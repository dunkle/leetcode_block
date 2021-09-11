class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            # print(l,r,mid)
            # 相等直接返回
            if nums[mid]==target:
                return mid
            # 旋转点在右侧,左侧有序
            if nums[l]<= nums[mid]:# 此处包含等号
                # 如果目标值在有序区间内，收敛边界
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                # 否则在另一个区间内
                else:
                    l = mid+1
                    # 旋转点在左侧，右侧有序
            else:
                # 如果查找值在有序数组中间，则收敛边界
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
