class Solution:
    def subsets(self, nums):
        results = []
        templist = []
        def backtrack(nums,templist, indexstart, results):
            if len(templist)==len(nums):
                return
            print("results", results)
            for i in range(indexstart, len(nums)):
                if nums[i] in templist:
                    continue
                templist.append(nums[i])
                print(templist)
                results.append(templist.copy())
                backtrack(nums, templist, i+1, results)
                templist.pop()
        backtrack(nums, templist,0, results)
        return results

A = Solution()
nums = [1,2,3]
A.subsets(nums)
