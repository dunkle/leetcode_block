import sys

# 这里写解决问题的代码，和LeetCode就完全一样了
def solve(arr):
    pass


if __name__ == '__main__':

    # 接收输入的逻辑，这里先把输入接收过来， 两种选择input()和sys.stdin.readline()
    group_nums = input()   #字符串形式，得转成int

    group_nums = int(group_nums)

    # 对于每一组
    for i in range(group_nums):
        # 接收每一组的输入, 这里不同的题目就不一样了，但一定记住我们接收的还是一行，这是一个字符串
        arr = sys.stdin.readline().strip().split(' ')
        # 元素转成int
        arr = list(map(int, arr))

        # 输入接收过来之后，这里最好打印下看看接收的是不是正确，这个很重要
        # print(arr)

        # 处理具体的问题了
        res = solve(arr)

        # 输出结果
        print(res)