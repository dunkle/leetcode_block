class Solution:
    def minArray(self, numbers) -> int:
        n = len(numbers)
        if n==1:
            return numbers[0]
        l = 0
        r = n-1
        # 二分查找 2，3，4，0，1，2
        # 正常有序数组 nums 比最右边大，比最左边小
        while l<r:
            mid = l+ (r-l)//2
            #中间元素比右边小，那么 肯定在左边，并且可能是当前所在位置
            if numbers[mid]<numbers[r]:
                r = mid
            #中间元素比右边大，那么 肯定在右边
            elif numbers[mid]>numbers[r]:
                l = mid+1
            # 如果相等，那么需要收缩右边界，即使右边界的值是最终值，但是数组中仍然存在该值，作为最小值，并不影响最后结果
            else:
                r = r-1
        return numbers[l]

a = Solution()
nums = [1,1,0,1]
res = a.minArray(nums)
print(res)

