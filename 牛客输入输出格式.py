'''
链接：https://ac.nowcoder.com/acm/contest/5652/A
来源：牛客网

题目描述
计算a+b
打开以下链接可以查看正确的代码
https://ac.nowcoder.com/acm/contest/5657#question
输入描述:
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。
输出描述:
输出a+b的结果
示例1
输入
1 5
10 20
输出
6
30
'''
def input_way():
    while True:
        try:
            a,b = map(int, input().split())
            print(a+b)
        except:
            break
def sysstdin_way():
    import sys
    while True:
        s = sys.stdin.readline().strip('\n')
        print(s)
        if s=='':
            break
        a,b = map(int, s.split())
        print(a+b)

'''
链接：https://ac.nowcoder.com/acm/contest/5652/B
来源：牛客网

输入描述:
输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)
输出描述:
输出a+b的结果
示例1
输入
2
1 5
10 20
输出
6
30
'''
def fun_input():
    n = int(input())
    for i in range(n):
        try:
            a, b = map(int, input().split())
            print(a+b)
        except:
            break
'''

'''