'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # s = "()[]{}"
        # s = "(]"
        # 如果是奇数个括号直接返回
        if len(s) % 2 == 1:
            return False
        n = len(s)
        if n==0:
            return True
        if n==1:
            return False
        stack = []
        for i in range(0,n):
            # print("s[i]:",s[i])
            # 栈为空说明前面的都可以能很好的配对
            if not stack:
                stack.append(s[i])
                continue
            # 栈不为空，如果出现以下符号，说明无法匹配，直接返回false
            if stack[0]==')' or stack[0]=='}' or stack[0]==']':
                return False
            # 排查了栈不以右括号结尾，说明都是左括号在栈里，需要判断当前字符是否有对应的右括号与之匹配，如果有，说明配对成功，栈弹出
            if (stack[-1]=='(' and s[i]==')') or (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']'):
                stack.pop()
                continue
            # if s[i]=="{" or s[i]=="[" or s[i]=='(':
            #如果 没有与之对应的右括号对应说明当前括号还是左括号，继续压栈
            stack.append(s[i])
        if not stack:
            return True
        return False
