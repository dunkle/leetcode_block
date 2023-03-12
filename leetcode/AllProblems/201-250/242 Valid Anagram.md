# 242. Valid Anagram

~~~python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if c in d:
                d[c] -= 1
            else:
                return False
            if d[c] < 0:
                return False
            
        for k in d:
            if d[k] != 0:
                return False
        return True
~~~

排序

~~~
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return False
            i, j = i+1, j+1
        
        if i == len(s) and j == len(t):
            return True
        return False
~~~

## Counter类

A [`Counter`](https://docs.python.org/3.8/library/collections.html#collections.Counter) is a [`dict`](https://docs.python.org/3.8/library/stdtypes.html#dict) subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The [`Counter`](https://docs.python.org/3.8/library/collections.html#collections.Counter) class is similar to bags or multisets in other languages.

Counter之间相减，只对包含在字典里的值进行操作，忽略不存在的值

![image-20200322134623261](.assert/image-20200322134623261.png)

~~~python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        return not (c1 - c2 or c2 - c1)
~~~

