'''
给定[-4,-2,0,1,5]（有序），返回X^2排序的结果，[0,1, 4, 16, 25]，时空复杂度O（N）



X^2+a*X, a is input



[-4, 0, 0, 5, 45] a=4
'''
def sort(nums, a):
    n = len(nums)
    if n==0:
        return nums
    for i in range(n):
        nums[i] = nums[i]+ a/2.0

    for i in range(n):
        if nums[i]>=0:
            break
    # print(i)
    res = []
    if i==0:
        while i<n:
            res.append(nums[i]*nums[i]-a*a/4.0)
            i+=1
        return res
    j = i-1
    # -2 1 2
    while i<n and j>=0:
        if (nums[i]*nums[i]-a*a/4.0)>=(nums[j]*nums[j]-a*a/4.0):
            res.append(nums[j]*nums[j]-a*a/4.0)
            j-=1
        else:
            res.append(nums[i]*nums[i]-a*a/4.0)
            i+=1
    while i<n:
        res.append(nums[i]*nums[i]-a*a/4.0)
        i+=1
    while j>=0:
        res.append(nums[j]*nums[j]-a*a/4.0)
        j-=1
    return res
nums = [-4,-2,0,1,5]
# nums = [0,1,3]
# nums = [-4,-3,-2]
a =4
# nums = [-4, 0, 0, 5, 45]
# a = 4
res = sort(nums, a)
print(res)


