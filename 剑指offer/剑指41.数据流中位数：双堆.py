'''
因为我们要取得中位数，所以只要关注前一半数字的最小值和后一段数字的最大值，采用堆来进行维护时间复杂度为O(logn)O(logn)。
由于python中只有小顶堆，那么B在构造时用小顶堆+元素取负的方法将其转换为大顶堆。
在构造堆时的目标，取中位数的时间复杂度O(1)O(1)：

如果元素为奇数个，那么中位数一定出现在AA的堆顶
偶数个时，中位数是(A(0) - B[0])/2 注意B中的元素是真实值的相反数。
由于我们始终要保证AA存整体的较大一半，B存整体的较小一半，且len(A) - len(B) = 0 or 1。那么分为两种情况：
len(A) = len(B)时,再加入一个元素时要使AA多一个，但加入的numnum的大小可能属于BB那一半，所以先加入BB，再把BB的最大值取出来放到AA中。
len(A) - len(B) = 1时，应将num加入B，但num大小可能属于A，故先加入A，再把A最小的元素加入BB
始终保持AA中存较大一部分，BB中存较小一部分(B中存的是相反数)。

空间复杂度: o(n)

作者：xiao-zhu-ssp
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/jian-zhi-41shu-ju-liu-zhong-wei-shu-shua-w7yh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.

        """
        self.A = []
        self.B = []
    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heapq.heappush(self.A , num)
            heapq.heappush(self.B , -heapq.heappop(self.A))
        else:
            heapq.heappush(self.B , -num)
            heapq.heappush(self.A , -heapq.heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0])/2.0

# 方法二 ，来一个数记一个数，维护一个数组为n的空间，对新来的数，二分查找插入。
# 中位数，则直接判断 数组个数 为奇数， 中间值，偶数就是 两者均值