# encoding: utf-8
# ------------ 美团 ---------------
# 两个数是相似的，当且仅当两个数位与不为0 e.g. 3的二进制011，5的二进制101，位与001，不为0，3和5相似
# 给定一个序列，求每一个数是否存在不相似数，若存在则返回1，否则-1
# 输入
# 4         # n个数
# 3 5 6 1   # 数值
# 输出
# -1 -1 1 1
import sys

def main():
   n = int(sys.stdin.readline().strip())
   num = list(map(int, sys.stdin.readline().strip().split(' ')))
   res = [-1]*n
   for i in range(n-1):
      if res[i] == 1:
         continue
      else:
         for j in range(i+1,n):
            if res[j] == 1:
               continue
            else:
               if not num[i]&num[j]:
                  res[i] = 1
                  res[j] = 1
   print(res)


main()
