# 9. Palindrome Number

判断一个整数是否为回文数字

注意：

1. 可能是负数，-123，此时不是回文
2. 翻转后，可能有前导0

~~~python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] in ['+', '-']:
            return False
        return x == int(s[::-1])
~~~

