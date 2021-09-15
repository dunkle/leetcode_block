'''
题目1：喜爱值最大
第一行：输入总金钱money，商品数量n
此后的n行：（每行代表一个商品，数值分别代表，商品价格、商品可买数量、商品喜爱值）
商品价格 商品数量 商品喜爱值
p1          n1       like1
p2          n2      like2
...
问：如何购买能让喜爱值最大
'''
def find_fav(inputstr, n, money):
    like, number, price = inputstr
    dp = [[0 for i in range(money+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(price[i], money+1):
            if j > price[i]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-price[i]]+like[i])
            else:
                dp[i][j] = dp[i-1][j]