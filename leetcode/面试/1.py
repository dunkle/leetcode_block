def jinzhi(arr):
    n = len(arr)
    dp = [0]*n
    for i in range(n-1,-1,0):
        if i==n-1:
            dp[i] =arr[i]
            continue
        dp[i] = max(dp[i-1], arr[i])
    for i in range(n):
        pass