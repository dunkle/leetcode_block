





# 13. Roman to Integer

~~~python
class Solution:
    def romanToInt(self, s: str) -> int:
        s2v = {
            "I":1,
            "V": 5,
            "X":10, 
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        def helper(s, i, c2, c3, s2v):
            if i != len(s)-1:
                if s[i+1] == c2:
                    return s2v[c2] - s2v[s[i]], 2
                elif s[i+1] == c3:
                    return s2v[c3] - s2v[s[i]], 2
            return s2v[s[i]], 1
        result, i = 0, 0
        while i < len(s):
            if s[i] == "I":
                t1, t2 = helper(s, i, "V", "X", s2v)
                result += t1
                i += t2
            elif s[i] == "X":
                t1, t2 = helper(s, i, "L", "C", s2v)
                result += t1
                i += t2
            elif s[i] == "C":
                t1, t2 = helper(s, i, "D", "M", s2v)
                result += t1
                i += t2
            else:
                result += s2v[s[i]]
                i+=1
        return result
    
~~~

从后遍历，保存后一个和前一个，如果符合特征，则减当前值即可
~~~python
class Solution:
    def romanToInt(self, s: str) -> int:
        s2v = {
            "I":1,
            "V": 5,
            "X":10, 
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        i, result = len(s), 0
        minus = ""
        while i > 0:
            c = s[i-1]
            if c == "I" and minus in ('V', 'X'):
                result -= s2v[c]
            elif c == "X" and minus in ('L', 'C'):
                result -= s2v[c]
            elif c == "C" and minus in ('D', 'M'):
                result -= s2v[c]
            else:
                result += s2v[c]
            i -= 1
            minus = c
        return result
~~~

