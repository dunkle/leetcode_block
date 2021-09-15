'''
选择排序
1、数组位置从0-n
2、每次找到第i小的元素放置位置 i-1位置处
'''
def select_sort(nums):
    n = len(nums)
    for i in range(n):
        ith = i
        for j in range(i+1, n):
            if nums[ith]>nums[j]:
                nums[ith], nums[j] = nums[j], nums[ith]
    print(nums)

arr = [1,3,4,2,5]
# arr = [1]
# arr = [1,1,1,1]
select_sort(arr)