![image-20210222200957622](../../../.assert/image-20210222200957622.png)

注意,**isnumeric函数无法判断负数**

~~~python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for s in tokens:
            if s.isnumeric() or (len(s) > 1 and s[0] == '-'):
                stack.append(int(s))
            else:
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(eval(f"{op1}{s}{op2}")))
        return stack[-1]
~~~

