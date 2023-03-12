# 14. Longest Common Prefix

![image-20200402205357497](../../../.assert/image-20200402205357497.png)



求给定字符串序列的而最长公共子串

### 垂直查找

以第一个字符串为基准，遍历字符串数组，判断当前字母是否相同

~~~python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        i, s = 0, ""
        while True:
            for st in strs:
                if i >= len(st):
                    return s
                if strs[0][i] != st[i]:
                    return s
            s += strs[0][i]
            i += 1
        return ""
~~~

### 水平查找

设$LCP(s_1, s_2)$为两个字符串的公共子串，则所有的公共字符串的公共字串为：
$$
LCP(s_1,\dots,s_n) = LCP(LCP(LCP(LCP(s_1, s_2), s_3), s_4), \dots, s_n)
$$
这种做法的缺点是，当最后有一个非常小的字符串时，前面要比较$n-1$次

~~~python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def LCP(s1, s2):
            prefix = s2
            while s1.find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
                if len(prefix) == 0:
                    return ""
            return prefix
        if len(strs) == 0:
            return ""
        
        lcp = strs[0]
        for s in strs[1:]:
            lcp = LCP(lcp, s)
        return lcp
~~~

### 分治法

将字符串数组分成两部分，分别求两边的公共子序列，然后合并

~~~python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def LCP(s1, s2):
            prefix = s2
            while s1.find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
                if len(prefix) == 0:
                    return ""
            return prefix
        
        def dac(strs):
            if len(strs) == 0:
                return ""
            if len(strs) == 1:
                return strs[0]
            # 这里注意要用len(strs)而不是len(strs)-1
            mid = len(strs)//2
            left = dac(strs[:mid])
            right = dac(strs[mid:])
            return LCP(left, right)
        
        return dac(strs)
~~~

### 二分查找

![image-20200402215119859](../../.assert/image-20200402215119859.png)

在第一个字符串中找到一个位置，使该位置之前的所有字符串均为公共子串。

~~~python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def LCP(s1, s2):
            prefix = s2
            while s1.find(prefix) != 0:
                prefix = prefix[0:len(prefix) - 1]
                if len(prefix) == 0:
                    return ""
            return prefix
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(c) for c in strs])
        low = 1
        high = min_len
        prefix = ""
        while low <= high:
            mid = (high + low) // 2
            tmp = strs[0][:mid]
            if all([c.find(tmp) == 0 for c in strs]):
                low = mid + 1
                prefix = strs[0][:mid]
            else:
                high = mid - 1
        return prefix
~~~

