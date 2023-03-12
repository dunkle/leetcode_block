给定一些候选数和一个target，求所有和为target的组合，其中组合中的每个数是从候选数种选出来的，候选数可选的次数是无限次。



完全背包问题，找到多个数，其和恰好为target，记录路径。

~~~python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [0] * (target + 1)
        path = [[] for _ in range(target+1)]
        
        dp[0] = 1
        path[0].append([])
        
        n = candidates[0]
        for i in range(n, target+1):
            if dp[i-n] == 1:
                dp[i] = 1
                for path1 in path[i-n]:
                    path[i].append(path1 + [n])
        
        for n in candidates[1:]:
            for i in range(n, target+1):
                if dp[i-n] == 1:
                    dp[i] = 1
                    for path1 in path[i-n]:
                        path[i].append(path1 + [n])
                    
        return path[-1]
~~~

