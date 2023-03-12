def pancakeSort(arr):
    if not arr or sorted(arr)==arr:
        return []
    res = []
    i = len(arr)
    print(arr)
    while i>1:
        max_idex = arr.index(max(arr[:i]))
        arr[:max_idex+1] = arr[:max_idex+1][::-1]
        print(arr, max_idex+1)
        arr[:i] = arr[:i][::-1]
        print(arr, i)
        res.extend([max_idex+1, i])
        i-=1

    print(res)
    return res
pancakeSort([1,3,2])
# pancakeSort([1,4,2,3])
