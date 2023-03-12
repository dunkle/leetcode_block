![image-20200901092147971](../../../.assert/image-20200901092147971.png)

给定一个字符串，找出其中最长的不重复字符子序列

利用一个字典记录每个字符出现的位置，遍历字符串，用当前字符作为最长不重复子序列的重点。

~~~python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat_dict = {}
        ret, start = 0, 0
        for i, c in enumerate(s):
            if c in repeat_dict:
                # 如果一个字符重复出现，则start为重复字符的下一个位置
                # 同时为了移除位于当前最长序列之外的重复字符，用max计算start
                start = max(repeat_dict[c]+1, start)
            
            # 最大位置为当前位置与start构成的最大长度
            ret = max(ret, i-start+1)
            repeat_dict[c] = i
        return ret
~~~

