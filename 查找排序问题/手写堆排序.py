'''
1、将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
2、将其与末尾元素进行交换，此时末尾就为最大值。可称为有序区，
3、然后将剩余n-1个元素重新构造成一个堆，估且称为堆区(未排序)。
这样会得到n个元素的次小值。重复执行，
有序区从:1--->n，堆区：n-->0，便能得到一个有序序列了
'''

def heapify(arr, n, i):
    '''
    从堆的最叶结点开始递归。直到递归到一个根节点，判断该根节点与其孩子节点的大小，三者或者两者比较大小
    将最大值记为 largest，如果 largest 是 根节点，递归结束， 如果不是根节点，将该节点与 根节点交换。
    largest 所指的节点 已经与根节点交换，因此需要更新以该节点为根节点的堆 大小变换，递归实现
    :return:
    '''
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.从最后一个节点开始，往最顶部根节点一直构造最大堆。
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 一个个交换元素，第0个节点为新堆的最大，通过交换，换到堆区部分。
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换 将根节点 与最后一个节点交换
        heapify(arr, i, 0) # 堆区数量改变


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print("%d" % arr[i]),
