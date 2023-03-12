# 395. Longest Substring with At Least K Repeating Characters

![image-20200426151107908](../../../.assert/image-20200426151107908.png)

在一个字符串中找到一个最长的连续公共子序列，子序列中的每个字符出现的次数都大于K。

依次找到一个出现次数小于k的位置，在这个位置切分，然后在左右两边递归寻找。

如果一个字符串中的的数量全都大于k，则返回该字符串的长度。

~~~python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter(s)
        start, cur, result = 0, 0, 0
        if all(c >= k for c in count.values()):
            return len(s)
        while cur < len(s):
            if count[s[cur]] < k:
                result = max(result, self.longestSubstring(s[start:cur], k))
                start = cur + 1
            cur += 1
        result = max(result, self.longestSubstring(s[start:], k))
            
        return result
~~~

