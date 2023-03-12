'''
稀疏矩阵元素的存储方式为
struct element
{
float data;
int row;
int col;
};
由几何算法生成了若干矩阵的元素std::vector<element> mat，
但顺序是乱的。请写出算法将mat中的元素调整为按行优先的顺序排列。
void genMat(std::vector<element>& mat)
'''
#coding=utf-8
import sys
#str = input()
#print(str)
# (2,1) (1,2)
def sort(arr):
    # list[(data0, 2,1), (data1, 1,2)]
    # list[(data, row, col),  ]
    def quicksort(arr, l,r):
        if l>r:
            return
        start, end = l,r
        pivot_row = arr[l][1]
        pivot_col = arr[l][2]
        pivot_data = arr[l][0]
        while l<r:
            while l<r and arr[r][1]>=pivot_row:
                if arr[r][1]==pivot_row and arr[r][2]<=pivot_col:
                    break
                r-=1
            arr[l][1] = arr[r][1]
            arr[l][2] = arr[r][2]
            arr[l][0] = arr[r][0]
            while l<r and arr[l][1]>=pivot_row:
                if arr[l][1]==pivot_row and arr[l][2]<=pivot_col:
                    break
                l+=1
            arr[r][1] = arr[l][1]
            arr[r][2] = arr[l][2]
            arr[r][0] = arr[l][0]

        arr[l][1] = pivot_row
        arr[l][2] =  pivot_col
        arr[l][0] = pivot_data
        quicksort(arr, start, l-1)
        quicksort(arr, l+1, end)





