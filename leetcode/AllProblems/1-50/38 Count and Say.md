# 38. Count and Say

![image-20200330104404614](../../../.assert/image-20200330104404614.png)

给定字符串，下一个字符串为字符数量+字符内容组成，求第N个字符串。

**思路**

从第一个字符串开始构造，不断地根据规则生成。

~~~python
class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(s):
            next_s = ""
            current = s[0]
            count = 0
            i, j = 0, 0
            while i < len(s):
                while j < len(s) and s[j] == s[i]:
                    count, j = count + 1, j + 1
                next_s = next_s + str(count) + s[i]
                i, count = j, 0
            return next_s
        s = "1"
        for _ in range(n-1):
            s = helper(s)
        return s
~~~

使用python中的itertools.groupby快速生成：

~~~python
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s)) # 根据unique属性将其分组
    return s
~~~

`itertools.groupby`(*iterable*, *key=None*)`是根据key将iterable中的元素分组，返回的是每一个组和对应的key，例如：

~~~python
from itertools import groupby

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print "A %s is a %s." % (thing[1], key)
    print " "
~~~

key默认为unique。