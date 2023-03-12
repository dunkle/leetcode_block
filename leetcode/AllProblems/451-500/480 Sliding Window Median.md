给定一个无序的数组和一个滑动窗口，求每个滑动窗口中的值。



在每个滑动窗口中都是一个无序的子数组，因此可以利用数组求中间值的方式求中位数。

利用数组求中间值可以使用两个堆，一个大顶堆和一个小顶堆。其中大顶堆保存小于等于中位数的值，小顶堆存放大于中位数的值。

当数组长度为奇数时，返回大顶堆的堆顶；如果为偶数则返回小顶堆的堆顶和大顶堆的堆顶平均值。

在本题中，仍可以利用这种方式，需要每个滑动窗口都创建两个堆求一次中位数。但由于滑动窗口每次滑动的过程中，都会新加入一个值，然后删除一个值，因此我们可以重复利用之前的两个堆。但在堆中删除一个元素是及其复杂的，所以，使用延迟删除。也即只有当被删除的元素到达堆顶时才移除，如果不在堆顶只需保证两个堆元素数量平衡即可。

~~~python
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_med(h1, h2, meds, k):
            # h1 big heap
            # h2 small heap
            meds.append(h2[0][0] if k & 1 else (h2[0][0]-h1[0][0])/2)
        # 将h1的顶部加入到h2中
        def move(h1, h2):
            x, i = heapq.heappop(h1)
            heapq.heappush(h2, (-x, i))
        # 初始化两个堆
        little, big = [], []
        medians = []
        # 将前k个元素先放入大顶堆中
        for i in range(k):
            heapq.heappush(big, (-nums[i], i))
        # 将大于等于中位数的数加入到小顶堆中，此时中位数位于小顶堆中
        for i in range(k-(k>>1)):
            move(big, little)
        # 获取第一个中位数
        get_med(big, little, medians, k)
        # 从第k个元素开始遍历
        for i,x in enumerate(nums[k:]):
            # x是新加入的元素
            # 如果比小顶堆的堆顶大，则加入到小顶堆中
            if x >= little[0][0]:
                heapq.heappush(little, (x, i+k))
                # nums[i]为要被删除的元素，如果位于大顶堆或在小顶堆堆顶，则删除大顶堆中的元素会造成二者不平衡
                # 因此将小顶堆中的一个元素放到大顶堆中
                # 为什么是小顶堆的堆顶也不平衡？？
                if nums[i] <= little[0][0]:
                    move(little, big)
            else:
                heapq.heappush(big, (-x, i+k))
                if nums[i] >= little[0][0]:
                    move(big, little)
            # 延迟删除小顶堆的元素
            while little and little[0][1] <= i:
                heapq.heappop(little)
            # 延迟删除大顶堆的元素
            while big and big[0][1] <= i:
                heapq.heappop(big)
                
            get_med(big, little, medians, k)
        return medians
~~~

