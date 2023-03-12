给出Pascal三角的第i行的值。

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row.append(row[-1])
            prev = row[0]
            for j in range(1, len(row)-1):
                prev, row[j] = row[j], prev+row[j]
        return row   
```

对一个数组进行不断的迭代。

观察三角的产生可以得到，每个数只用当前数和前一个数即可生成，因此用一个变量保存前一个状态，就可以不断更新了。