'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 
提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def merge(self, intervals):
        m = len(intervals)
        if m==0:
            return []

        # 针对元素的左边界排序
        def quicksort(l, r):
            if l>r:
                return
            start = l
            end = r
            pivot = intervals[l][0]
            pivotend = intervals[l][1]
            while l<r:
                while l<r and intervals[r][0]>pivot:
                    r-=1
                intervals[l][0] = intervals[r][0]
                intervals[l][1] = intervals[r][1]
                while l<r and intervals[l][0]<=pivot:
                    l+=1
                intervals[r][0] = intervals[l][0]
                intervals[r][1] = intervals[l][1]
            intervals[l][0] = pivot
            intervals[l][1] = pivotend
            # 快排
            quicksort(start, l-1)
            quicksort(l+1,end)

        quicksort(0, len(intervals)-1)
        print(intervals)
        # 用一个数组存储结果，数组里的结果都是无重叠的区间
        res = [intervals[0]]
        i=1
        for i in range(1, m):
            # 把新的区间，和数组结果中最后一个区间合并
            tmp = res[-1]
            # [a,b] [c, d] 两个区间合并 其中 c>=a
            # 如果第二个区间起始位置 c>b 说明两个区间无重叠
            if intervals[i][0]>tmp[1]:
                res.append(intervals[i])
            # 如果 c<=b and b<=d说明两个区间有交叉 -》 [a,d]
            elif intervals[i][0]<=tmp[1] and intervals[i][1]>=tmp[1]:
                # 把最后一个区间弹出，再把新区间放进去
                res.pop()
                res.append([tmp[0], intervals[i][1]])
            # d<=b 说明 [a,b]区间包含了[c,d]区间，直接跳过即可
            elif intervals[i][1]<=tmp[1]:
                continue
        return res

