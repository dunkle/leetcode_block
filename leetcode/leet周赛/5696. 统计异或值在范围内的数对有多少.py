class Solution:
    def countPairs(self, nums, low: int, high: int) -> int:
        lowbit = 0
        n = 0
        while True:
            n = 2**lowbit
            if n >=low:
                break
            lowbit += 1
        lowbound = n//2
        n =0
        highbit = 0
        while True:
            n = 2**highbit
            if n >= high:
                break
            highbit += 1
        highbound = n

        print("low:high", low, high)
        nums = sorted(nums)
        print(nums)
        print(lowbound, highbound)
        lowboundindex, highboundindex = 0, 0

        for i in range(len(nums)):
            if nums[lowboundindex]<=lowbound:
                lowboundindex+=1
            if nums[highboundindex]<=highbound:
                highboundindex+=1
        # lowboundindex -=1
        print("index", lowboundindex, highboundindex)
        allpairnum = lowboundindex * (highboundindex-lowboundindex)
        print("all", allpairnum)
        for i in range(lowboundindex, highboundindex):
            for j in range(i+1, highboundindex):
                print("num[i], num[j]: ", nums[i], nums[j])
                if low<=nums[i] ^ nums[j]<=high:
                    allpairnum+=1
        for i in range(highboundindex, len(nums)):
            for j in range(i+1, len(nums)):
                if low<=nums[i] ^ nums[j]<=high:
                    allpairnum+=1
        for i in range(lowboundindex):
            for j in range(i+1, lowboundindex):
                if low<=nums[i] ^ nums[j]<=high:
                    allpairnum+=1
        return allpairnum

a = Solution()
nums = [1,4,2,7]
low = 2
high = 6
# nums = [9,8,4,2,1]
# low = 5
# high = 14
print(a.countPairs(nums, low, high))