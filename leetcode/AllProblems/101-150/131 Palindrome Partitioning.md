# 131. Palindrome Partitioning

![image-20200414214812678](../../.assert/image-20200414214812678.png)

给定一个字符串，将字符串切分，使得每个部分均为回文串。

回溯法，从头开始不断截取字符串，如果是回文，则结果为当前串加剩下字符串的分割。

~~~python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        
        for i in range(1, len(s)+1):
            if self.is_par(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
        
        
    def is_par(self, s):
        return s == s[::-1]
~~~

