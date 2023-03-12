# 171. Excel Sheet Column Number

python中字符转换为ASCII码：

~~~shell
>>> chr(97)
'a'
>>> ord('a')
97
~~~

~~~python
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i, c in enumerate(reversed(s)):
            v = ord(c) - ord('A') + 1
            result += v * (26**i)
        return result 
~~~

