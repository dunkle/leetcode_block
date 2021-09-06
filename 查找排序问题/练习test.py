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

def adjustheap(heap, k):
    for i in range(k-1,-1, -1):
        heapfy(heap, i,k)


arr = [2, 1,8,5,4,3,7]
m = len(arr)
k = 3
heap = arr[0:k]
adjustheap(heap,k)
print(heap)
for i in range(k,m):
    if arr[i]>heap[0]:
        heap[0] = arr[i]
        adjustheap(heap,k)
print(heap)