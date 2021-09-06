'''
快速排序

需要指定一个pivot
当指定最左边作为pivot值时，需要从右边开始找 小于 pivot的值，将左边的left值 替换为 右边的值，
第一次为pivot，因此可以直接覆盖掉
之后再从左边找大于pivot的值，将右边的right 替换掉 左边的值

当循环停止时，代表 l==r 指针所指的位置时pivot的值，对其赋值即可

递归调用左右两边的数组值即可

'''

def quicksort(arr, l, r):
    start, end = l, r
    if l>r:
        return
    pivot = arr[l]
    while l<r:
        while l<r and arr[r]>=pivot:
            r-=1
        arr[l] = arr[r]
        while l<r and arr[l]<pivot:
            l+=1
        arr[r] = arr[l]
    arr[l] = pivot
    quicksort(arr, start, l-1)
    quicksort(arr, l+1, end)
arr = [1,3,4,2,5]
arr = [1]
arr = [1,1,1,1]
quicksort(arr, 0, len(arr)-1)
print(arr)