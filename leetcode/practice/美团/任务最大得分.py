# encoding: utf-8
import sys
# ------------ 美团 ---------------
# 现在一共有n个任务，每个任务k子任务，每个任务的第i个子任务需要的时间都是ti
# 共有时间m，每完成一个子任务，获得p分，每完成一个完整的任务，额外获得q分，不可重复完成，求最大收益
# 输入1
# 3 2 8    # n = 3；k = 2；m = 8
# 3 1      # p = 3；q = 1
# 9 5      # t1 = 3；t2 = 1
# 输出1
# 3        # 最大总得分
# 输入2
# 2 2 3
# 1 2
# 1 1
# 输出2
# 5
# ----------- dp -----------------------


def main():
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    n, k, m = tmp[0],tmp[1],tmp[2]
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    p,q = tmp[0],tmp[1]
    time = list(map(int, sys.stdin.readline().strip().split(' ')))
    time.sort() # 从小到大,后续每个时刻选择子任务时，若while的 当前时刻i < time[j] ，不需要再遍历-------优化
    if k == 1: # 只有一个子任务，不需要选择子任务，每次完成收益都是p+q
        print(m//time[0]*(p+q))
    else: # 有多个子任务
        dp = [0]*(m+1)  # 当前最大得分，下标和时刻m相对应，所以下标0不做考虑
        completed = [0]*k # 子任务完成次数，若每个子任务的次数>=1,可以计算q，之后次数全部-1
        start = time[0] # 完成的第一个任务的时刻 start 是 花费时间最小的子任务完成时间 time[0]
        completed[0] = 1 # 完成第一个子任务一次
        dp[start] = p # 第一个子任务得分为p,因为有多个子任务，所以此时不考虑q
        for i in range(start+1,m+1):
            j = 0 # 第一个子任务 index = 0
            dict = {} # 记录每一个子任务完成后是否可以直接计算q
            score = [] # 本时刻完成每个子任务所对应的分数
            while j < k and (i - time[j]) >= 0 : # 短路判断，所以先判断是否越界 然后是(i - time[j]) >= 0
                completed[j] += 1  # 假设当前完成子任务 j
                h = 0
                while h<k and completed[h]: # 短路判断，所以先判断是否越界，再判断completed[h]
                    h += 1
                completed[j] -= 1 # 取消假设
                #子任务 j
                if h == k: # 子任务全部完成
                    tmp = dp[i - time[j]] + p + q # 选择完成j子任务后，i时刻的总收益
                    score.append(tmp) # 加入score，后续判断选择哪个子任务收益最高
                    dict[j] = True # 选择完成j任务后，所有子任务都完成一遍
                else: # 子任务没有全部完成
                    tmp = dp[i - time[j]] + p
                    score.append(tmp)
                    dict[j] = False
                j += 1 # 下一个子任务
            # 更新本时刻最终得分 dp[i-1]
            if dp[i-1]>max(score):
                dp[i] = dp[i-1] # 此时可没有完成任何子任务，而是在完成某个任务的过程中，所以收益和上一个时刻一样
            else: # 此时完成子任务
                dp[i] = max(score)
                index = score.index(max(score)) # 子任务index
                if dict[index]: # 完成该子任务后，所有子任务都完成了一遍
                    for i in range(k): # 更新completed
                        completed[i] -= 1
                completed[index] += 1 # 补上多减的completed[index]
        print(dp[m])

main()
