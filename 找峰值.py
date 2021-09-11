
import io
import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# #str = input()
# #print(str)
# print('hello world!')

def peak_find(nums,start, end):
    mid = (start+end)//2
    # 大于两侧直接找到
    if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        return mid
    # 向左边找
    if nums[mid-1]>nums[mid] and nums[mid]>nums[mid+1]:
        return peak_find(nums, start,mid-1)
    # 否则向右边找
    return peak_find(nums, mid+1, end)

nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
nums = [1,2,1]
nums = [1]
nums = [1,2]
nums = [1,2,3]
if len(nums)==1:
    print(0)
elif len(nums)==2:
    if nums[0]>nums[1]:
        print(0)
    else:
        print(1)
res = peak_find(nums, 0, len(nums)-1)
print(res)