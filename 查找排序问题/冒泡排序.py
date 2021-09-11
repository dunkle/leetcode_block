'''
冒泡排序
两重循环
第一重循环，从最后一个开始，一直往前，代表依次排好的顺序，从后往前固定。
第二重循环，从第一个开始，一直往后，依次两两交换，直到第一重循环的最后。
'''
def bubblesort(arr):
    n = len(arr)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if arr[i]> arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
arr = [1,3,4,2,5]
# arr = [1]
# arr = [1,1,1,1]
bubblesort(arr)