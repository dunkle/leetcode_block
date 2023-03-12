# 454. 4Sum II

![image-20200407142241886](../../.assert/image-20200407142241886.png)

给定4个等长的数组，从4个组中取一个数，求相加为0的数对数量

## Hashtable

本题与2Sum类似，求出A和B中所有的数对和，求出C和D中所有的数对和，找二者相加为0的数量即可。坑在于，不同的数对和可能为一个值，因此字典中应为构成该和的数对数量

~~~python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        num_dict = {}
        result = 0
        for c in C:
            for d in D:
                s = c+d
                if s not in num_dict:
                    num_dict[s] = 1
                else:
                    num_dict[s] += 1
        for a in A:
            for b in B:
                target = 0 - (a+b)
                if target in num_dict:
                    result += num_dict[target]
        return result
~~~

~~~python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
~~~

