# 递归解法
def binary_search(arr, target):
    if len(arr)==0:
        return False
    mid = len(arr)//2
    if arr[mid]>target:
        binary_search(arr[:mid], target)
    elif arr[mid]<target:
        binary_search(arr[mid+1:], target)
    else:
        return True
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
flag = binary_search(testlist, 3)
print(flag)
# print(binary_search(testlist, 13))

# 迭代二分解法
class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            else:
                right = mid
        if nums[left]==target:
            return left
        else:
            return -1


# 边界值写法
def bin_search(self, nums, target: int) -> int:
    left = 0
    right = len(nums)-1
    # 取等号 left ==right 代表 最后l==r的中间值需要判断
    while left<=right:
        # mid 的标准写法 相减防止溢出
        mid = left + (right-left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid-1
        else:
            return mid
    return -1