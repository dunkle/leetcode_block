# 特别大的数组，取前k个数字
# 堆排序取前k个数字
#时间复杂度 O(nlgk)
def sift(li, low, high):
    i = low
    j = 2*i+1
    tmp = li[low]
    while j<=high:
        if j+1<=high and li[j+1]<li[j]:
            j+=1
        if li[j]<tmp:
            li[i] = li[j]
            i=j
            j=2*i+1
        else:
            break
        li[i] = tmp

def topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2, -1,-1):
        sift(heap,i,k-1)
    # 建堆
    for i in range(k, len(li)):
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap,0, k-1)
    # # 最大堆 排序顺序输出
    for i in range(k-1, -1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap
arr = [4,5,1,6,2,7,3,8]
res = topk(arr,3)
print(res)
