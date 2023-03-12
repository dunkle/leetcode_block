# 36. Valid Sudoku

![image-20200412135312889](../../../.assert/image-20200412135312889.png)

判断一个数独是否有效：

1. 每一行必须包含1-9没有重复
2. 每一列必须包含1-9没有重复
3. 每一个3x3的单元必须包含1-9没有重复

一个有效的数独不代表可解，因此只需判断每行每列每单元是否有重复的数字即可。

range的用法：

```python
range(start, stop[, step])
```

从一个二维数组中取出每列：

~~~python
for c in zip(*board):
~~~



~~~python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid_unit(unit: List) -> bool:
            unit = [c for c in unit if c != "."]
            # print(unit)
            # print(set(unit))
            return len(set(unit)) == len(unit)
        
        def is_valid_row(board: List[List[str]]):
            for b in board:
                if not is_valid_unit(b):
                    return False
            return True
        
        def is_valid_col(board: List[List[str]]):
            for c in zip(*board):
                if not is_valid_unit(c):
                    return False
            return True
        
        def is_valid_square(board: List[List[str]]):
            for i in [0, 3, 6]:
                for j in [0, 3, 6]:
                    square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not is_valid_unit(square):
                        return False
            return True
            
        
        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
    

~~~

