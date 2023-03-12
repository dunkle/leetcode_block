class Solution:
    def minSideJumps(self, obstacles) -> int:
        n = len(obstacles)
        dp = [[float('inf') for j in range(3)] for i in range(n)]
        dp[0] = [1,0,1]
        for i in range(1, n):
            for j in range(3):
                if obstacles[i] == j + 1:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
            for j in range(3):
                for k in range(3):
                    if obstacles[i] == j + 1 or j == k:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i][k] + 1)
        # print(dp)
        return min(dp[-1])