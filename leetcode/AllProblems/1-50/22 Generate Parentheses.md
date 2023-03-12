# 22. Generate Parentheses

![image-20200402231034981](../../../.assert/image-20200402231034981.png)

给定一个数N，输出N对括号的所有组合

## BFS

N对括号，左括号和右括号的数量均为N，根据括号的规则向字符串中添加括号即可，一共有4种情况：

1. r == 0,此时括号全部使用完，添加到result中
2. l == 0, r > 0 只能添加右括号
3. l >0 and l < r 左右括号均可添加
4. l >0 and l == r，只能添加左括号

~~~python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        stack.append(("(", n-1, n))
        while len(stack) != 0:
            s, l, r = stack.pop()
            if r == 0:
                result.append(s)
                continue
            if l == r:
                stack.append((s+"(", l-1, r))
            if l > 0 and l < r:
                stack.append((s+"(", l-1, r))
                stack.append((s+")", l, r-1))
            if l == 0 and l < r:
                stack.append((s+")", l, r-1))
        return result
~~~

**递归的方式**

~~~python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        def helper(s, l, r, n, result):
            if len(s) == 2*n:
                result.append(s)
                return
            if l < n:
                helper(s+"(", l+1, r, n, result)
            if r < l:
                helper(s+")", l, r+1, n, result)
        helper("", 0, 0, n, result)
        return result
~~~

**Closure Number**

先固定一对括号，然后剩下的括号可以放到当前括号的里面和外面，剩下的括号数量为n-1，分配给外面和里面

~~~python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-c-1):
                    ans.append('({}){}'.format(left, right))  
        return ans
~~~



