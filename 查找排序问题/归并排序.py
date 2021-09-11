'''
归并排序包含两个 函数
一个负责把数组拆分成两个数组，一个负责把两个数组合并成一个数组

因此 拆分数组传入参数 是数组 arr即可
    合并数组传入参数 是两个数组 left 和 right

    合并数组需要有返回值，返回合并好的数组
    拆分数组也需要有返回值，需要返回拆分后的数组

    递归终止条件是数组内元素个数为1 即返回

'''
def partition(arr):
    lenth = len(arr)
    if lenth<2:
        return arr
    mid = lenth//2
    left = partition(arr[0:mid])
    right = partition(arr[mid:])
    return merge(left, right)
def merge(left, right):
    mergearr = []
    i, j = 0, 0
    lenleft = len(left)
    lenright = len(right)
    while i<lenleft and j<lenright:
        if left[i]<right[j]:
            mergearr.append(left[i])
            i+=1
        else:
            mergearr.append(right[j])
            j+=1
    mergearr += left[i:]
    mergearr += right[j:]
    return mergearr
# arr = [1,3,4,2,5]
# arr = [1]
arr = [1,1,1,1]
part = partition(arr)
print(part)

