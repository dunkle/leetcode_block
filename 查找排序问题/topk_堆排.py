class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        #堆化，调整左右节点，变为最小堆
        def heapfy(arr, i, n):
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] < arr[smallest]:
                smallest = l
            if r < n and arr[r] < arr[smallest]:
                smallest = r
            if smallest!=i:
                arr[smallest], arr[i] = arr[i], arr[smallest]
                heapfy(arr,smallest,n)

        # 维护这个最小堆
        def adjustheap(heap, k):
            for i in range(k-1,-1, -1):
                heapfy(heap, i,k)


        # arr = [2, 1,8,5,4,3,7]
        arr = nums
        m = len(arr)
        # k = 3
        # 初始化这个最小堆
        heap = arr[0:k]
        adjustheap(heap,k)
        # print(heap)
        # 对 后续数组元素继续添加到堆里，进行维护
        for i in range(k,m):
            # 只有比堆的最小元素大才可能变为前k大的数
            if arr[i]>heap[0]:
                #第一个元素为最小的元素，替换掉，重新维护堆
                heap[0] = arr[i]
                adjustheap(heap,k)
        # 堆的大小为k，第一个为最小的元素，也就是第k大的元素
        return heap[0]