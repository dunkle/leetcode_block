# 347. Top K Frequent Elements

![image-20200403144539794](../../.assert/image-20200403144539794.png)

给定一个数组，求出现次数最多的前K个数组。

先遍历一边数组得到每个数出现的次数，时间复杂度为O(N),然后对其进行按照次数进行排序，取前k个数，时间复杂度为O(NlogN)

~~~python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        tmp = []
        for key, v in d.items():
            tmp.append((key, v))
        tmp = sorted(tmp, key=lambda x:x[1], reverse=True)
        result = [x[0] for x in tmp[:k]]
        return result
~~~

## Counter

使用python的counter类

counter可以统计数组中数出现的个数，most_common返回出现最多的几个数。

~~~python
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [key for key,value in counter.most_common(k)]
~~~

