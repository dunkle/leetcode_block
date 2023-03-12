# coding=utf-8
# ------------ 百度 ---------------
# 初始状态下，所有括号都是红色，把部分括号染成绿色或蓝色，
# 要求：
#     每一对相匹配的括号必须有，且只有一个括号可以被染成绿色/蓝色，另一个保持红色
#     相邻的括号不能同为绿色/蓝色
# 输入
#     第一行：括号序列的长度n
#     第二行：长度为n的括号字符串
# 6
# ((()))
#
# 输出
#     共有多少种染色方案
# 36
import sys
def main():
    # n = int(sys.stdin.readline().strip()) #括号序列的长度n
    # string = sys.stdin.readline().strip() #长度为n的括号字符串 (()())
    n = 6
    string = '((()))'
    stack = []
    memo=[]
    for i in range(n):
        if string[i]=='(':
            stack.append(i) # 左括号下标 压栈
        else:
            ind=stack.pop() # 左括号下标 出栈
            memo.append((ind,i))  # 每对括号的（左括号下标，右括号下标）包含：由内向外；并列：从左向右
    print(memo)
    dp=[[0,0,0,0] for i in range(len(memo))] # [第几个括号][染色方案] len(memo)✖️3
    # dp[0]为最里面的括号，提前赋值
    dp[0][0] = 1 #左括号为红色，右括号为绿色
    dp[0][1] = 1 #左括号为红色，右括号为蓝色
    dp[0][2] = 1 #左括号为绿色，右括号为红色
    dp[0][3] = 1 #左括号为蓝色，右括号为红色
    for i in range(1,len(memo)):
        if memo[i][0]<memo[i-1][0]: # 如果当前括号里面还有括号：
            # 左括号为红色，右括号为绿色, 取决于里面右括号红色/蓝色
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            # 左括号为红色，右括号为蓝色, 取决于里面右括号红色/绿色
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]
            # 左括号为绿色，右括号为红色, 取决于里面左括号红色/蓝色
            dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3]
            # 左括号为蓝色，右括号为红色, 取决于里面左括号红色/绿色
            dp[i][3] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
        else: # 如果当前括号在前面计算过的括号的右边，如（（））（）中的右边那对括号：
            # 左括号为红色，右括号为绿色, 取决于左边右括号红色/蓝色/绿色
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            # 左括号为红色，右括号为蓝色, 取决于左边右括号红色/蓝色/绿色
            dp[i][1] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            # 左括号为绿色，右括号为红色, 取决于左边右括号红色/蓝色
            dp[i][2] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            # 左括号为蓝色，右括号为红色, 取决于左边右括号红色/绿色
            dp[i][3] = dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]
    print (dp[len(memo)-1][0]+dp[len(memo)-1][1]+dp[len(memo)-1][2]+dp[len(memo)-1][3]) #染色总方案

main()
