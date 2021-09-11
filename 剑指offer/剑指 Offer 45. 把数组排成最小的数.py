class Solution:
    def minNumber(self, nums) -> str:
        '''
        排在前面的 x <y <-> xy < yx
        (10 *x +y) < (10*y + x)
        :param nums:
        :return:
        '''
        n = len(nums)
        if n==1:
            return str(nums[0])
        # 将输入数组映射成字符串
        nums = [str(num) for num in nums]

        # 快排求排序
        def quicksort(arr, l,r):
            if l>r:
                return
            start, end = l, r
            pivot = arr[l]
            while l<r:
                while l<r and arr[r]+pivot>=pivot+arr[r]:
                    r-=1
                arr[l] = arr[r]
                while l<r and arr[l]+pivot<pivot+arr[l]:
                    l+=1
                arr[r] = arr[l]
            arr[l] = pivot
            quicksort(arr, start, l-1)
            quicksort(arr, l+1, end)


        # print(nums)
        quicksort(nums, 0, len(nums)-1)
        return "".join(nums)

a =  Solution()
nums = [3,30,34,5,9]
nums = [2, 10]
res = a.minNumber(nums)
print(res)