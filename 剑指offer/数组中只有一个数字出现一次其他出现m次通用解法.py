class Solution:
    def singleNumber(self, nums, m) -> int:
        res = [0]*32
        for num in nums:
            for i in range(32):
                if num&1:
                    res[i] +=1
                num>>=1
        results = 0
        for i in range(32):
            if i%m==1:
                i >>=1
                results|=i
            else:
                pass
        return results

a = Solution()
nums = [1,2,2,2]
m = 3
res = a.singleNumber(nums, m)
print(res)