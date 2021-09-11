'''
判断的范围越来越小，所以小长度开始遍历，逐步化解更大范围的问题，有分治的思想.
'''
def helper(self, ns) :
    N = len(ns)
    dp = [[0] * N for _ in range(N+1)]
    for l in range(N): # 长度从小到大
        for i in range(N-l): # 以 i 为 开头
            j = i + l           # 以 j 为 终点
            for k in range(i,j): # 以 k 为分割点，进行分治
                pass
                #// Todo 业务逻辑

