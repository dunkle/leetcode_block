# 118. Pascal's Triangle

~~~python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            result.append([1]*(i+1))
            for j in range(1, i):
                result[-1][j] = result[-2][j-1] + result[-2][j]
        return result
~~~

注意这里的i是当前行的长度-1