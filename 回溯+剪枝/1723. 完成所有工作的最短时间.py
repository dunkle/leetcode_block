class Solution:
    def minimumTimeRequired(self, jobs, k: int) -> int:
        #每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r = max(jobs), sum(jobs)

        # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
        arr = sorted(jobs)
        # print(jobs)
        def backtrack(groups, jobs, limit):
            # 当所有的jobs都被分配完成之后，方案是可行的直接True
            if not jobs:
                return True
            # 选择一个工作
            now = jobs.pop()
            # 依次给对应的工人完成，遍历所有可能性
            for i in range(k):
                # 如果可以放入这个工人的时长，则继续往下
                if groups[i]+now<=limit:
                    groups[i]+=now
                    if backtrack(groups, jobs, limit):
                        return True
                    groups[i]-=now
                # 此处重要的剪枝，意味着，将工作给对应的工人做的时候，需要优先给没有活干的人。
                # 也就是当分配完工作之后，对应的工人工作时间为0 说明这个工人及之后的工人都是无活可干的人直接break
                if groups[i]==0:
                    break
            # 返回原状态，说明按照当前工作分配，无法满足最低limit的限制
            jobs.append(now)
            return False

        while l<r:
            # 此处采用二分的方法判断，可以大大缩减时间限制
            mid = (l+r)//2
            groups = [0]*k
            # 这个位置需要用copy 每次找新的边界时需要重新分配工作，避免之前的分配状态未结束
            jobs = arr.copy()
            if backtrack(groups, jobs, mid):
                r= mid
                print("1:",jobs)
            else:
                l = mid+1
                print("2", jobs)
        return l

a = Solution()
jobs = [1,2,4,7,8]
k = 2
res = a.minimumTimeRequired(jobs,k)
print(res)