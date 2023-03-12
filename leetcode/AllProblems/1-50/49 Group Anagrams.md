# 49. Group Anagrams



![image-20200404001508076](../../../.assert/image-20200404001508076.png)

给定一个字符串数组，将含有相同字母的元素分到一组

## 以排序后的字符串为key分组

含有相同字母的字符串排序后的字符串是一样的。

~~~python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            t = "".join(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]
        return d.values()
~~~

时间复杂度为$O(NKlogK)$,N为数组的个数，遍历数组；K为最长字符串的长度$O(KlogK)$是排序的时间复杂度。

## 以字符串内字符出现的次数为Key分组

由于全是字母而且均为小写字母，因此可以构造一个长度为26的tuple记录当前字符串中每个字符出现的次数，以这个tuple作为key

~~~python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            alphabet = [0]*26
            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            d[tuple(alphabet)].append(s)
        return d.values()
~~~

defaultdict的行为与dict相同，但是可以不用进行初始值判断

具体可查看[defaultdict](https://docs.python.org/3.8/library/collections.html#defaultdict-objects)

