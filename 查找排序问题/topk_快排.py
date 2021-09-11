#coding=utf-8
import sys
#str = input()
#print(str)
# 给y
#  1 2 3 4 -> 2
# 1 2   3 4
def findK(arr, K):
    def quicksort(arr,l,r,K):
        start, end =l,r
        if l >r:
            return
        pivot = arr[start]
        while l<r:
            while l<r and arr[r]>=pivot:
                r-=1
            arr[l] =arr[r]
            while l<r and arr[l]<pivot:
                l+=1
            arr[r] = arr[l]
        arr[l] = pivot
        print("arr:", arr)
        # lenth = l-start+1
        lenth = l+1
        if K<lenth:
            quicksort(arr, start, l-1, K)
        elif K>lenth:
            quicksort(arr, l+1, end, K)
        else:
            print(arr[l+1])
    return quicksort(arr, 0, len(arr)-1,K)
arr = [1,3,2,4,5]
# 第2 大，数组长度为5 第 3 小。
K = 2

# 1 3 2 4
# 1   3 2 4
# k 下标为3
# 1 2 3 4 5
#2  3 4
if K> len(arr):
    print("K 大于数组最大长度")
else:
    # res = findK(arr, len(arr)-K)
    res = findK(arr, K)
#     print(res)
# n- > n/2 -> n/4
#lgn

            