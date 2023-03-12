class Solution:
    def subsets(nums):
        if len(nums) == 0:
            return []
        n = len(nums)
        res = []

        def dfs(idx, tmp_list):
            res.append(tmp_list)
            print(res)
            for i in range(idx, n):
                # tmp_list.append([nums[i]])
                dfs(i + 1, tmp_list+ [nums[i]])

        dfs(0, [])
        return res


Solution.subsets([1, 2, 3])
c = []
a = [1, 2]
b = [3]
# print(c+a+b)



