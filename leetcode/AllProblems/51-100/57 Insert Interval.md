给定一系列非重叠的区间，插入一个新区间，如果重叠就将其合并。



将所有区间分为严格小于、严格大于和重叠三个类别，对于左边和右遍的区间直接保存到结果集中即可，对于重叠的区间需要进行合并。

~~~python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        s, e = newInterval[0], newInterval[1]
        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
                
        return left + [[s, e]] + right
~~~

