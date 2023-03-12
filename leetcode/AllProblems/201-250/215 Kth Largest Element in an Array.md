# 215. Kth Largest Element in an Array

![image-20200406164056902](../../../.assert/image-20200406164056902.png)

求一个无序列表中第K大的元素

使用heap，也即优先队列，将所有元素push到堆中，pop到第K个元素即可。

python中的heap都是最小堆，因此需要转换一下元素的大小关系。

python中heap是一个操作，这个操作主要应用于一个链表中。

~~~python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for n in nums:
            heapq.heappush(hq, -1*n)
        for _ in range(k):
            v = heapq.heappop(hq)
        return -1*v
~~~

## 快速选择算法

利用快速排序的划分模块，得到哨兵元素的坐标，与k比较，如果大，说明在哨兵的左侧，如果小，说明在哨兵的右侧。

注意边界元素

~~~python
class Solution:
    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot  
    # low左边的元素都比最右侧元素小，右遍的元素都比右侧元素大
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
~~~

