class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        '''
        从右上角开始找，找不到划掉一行或者一列
        :param matrix:
        :param target:
        :return:
        '''
        m = 0
        n = len(matrix[0])-1
        while m<len(matrix) and n>=0:
            if matrix[m][n]>target:
                n-=1
            elif matrix[m][n]<target:
                m+=1
            else:
                return True
        return False