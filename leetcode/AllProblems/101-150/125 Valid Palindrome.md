# 125. Valid Palindrome

头尾遍历字符串，判断是否相等，若不想等：

1. 若二者为字母数字，return False
2. 移动指针

~~~python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        h, t = 0, len(s)-1
        def hleper(s):
            return s.isalnum()
        while True:
            while h < t and s[h] == s[t]:
                h += 1
                t -= 1
            if h >= t:
                break
            if hleper(s[h]) and hleper(s[t]):
                return False
            if not hleper(s[h]):
                h += 1
            if not hleper(s[t]):
                t -= 1
        return True
~~~

首先排除其中的非字母数字字符，然后将其反转，判断两个list是否相等即可

~~~python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return [c.lower() for c in s if c.isalnum()] == [c.lower() for c in s[::-1] if c.isalnum()]
        t = [c.lower() for c in s if c.isalnum()]
        return t == list(reversed(t))
~~~

