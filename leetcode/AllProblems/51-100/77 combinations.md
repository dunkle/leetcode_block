给定n和k，输入1-n中所有长度为k的组合，也即求$C_n^k$

~~~python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(nums, path):
            if len(path) == k:
                result.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])

        dfs([i for i in range(1, n+1)], [])
        return result
~~~

时间复杂度为$O(C_n^k)$

