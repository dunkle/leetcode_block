~~~python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = Counter(s)
        for i, c in enumerate(s):
            if m[c] == 1:
                return i
        return -1
        
        # hash表法时间复杂度为O(N),空间复杂度为O(N)
        ha = dict()
        for c in s:
            if c in ha:
                ha[c] += 1
            else:
                ha[c] = 1
        for i, c in enumerate(s):
            if ha[c] == 1:
                return i
        return -1
        
        
        # 暴力求解是O（N^2)，空间复杂度为O(N)
        for i, c in enumerate(s):
            if c not in s[:i]+s[i+1:]:
                return i
        return -1
~~~

更快的方法

~~~python
   def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        # 这里注意len(index)的判断
        return min(index) if len(index) > 0 else -1
~~~

Its only faster because s.index is a C function that python is calling. So you are changing the python loop to be the 26 characters, and the C loop is doing the heavy lifting searching the string. From an algo perspective this is slower than the others. But good to know for python users for runtime speedup