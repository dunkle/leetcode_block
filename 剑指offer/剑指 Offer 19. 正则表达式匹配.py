'''
剑指 Offer 19. 正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        # 第一个字母是否匹配, s不为空 并且 p[0]如果是. 则可以任意匹配，否则与 s[0] 比较是否匹配
        first_match = bool(s and p[0] in {s[0],'.'})
        # 第一个字母匹配成功
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            # 第一种情况 * 不与任何字符匹配，因此 s 和 p的第三个字符之后开始比较
            # 如果 * 与s的第一个字符匹配，那么可以一直匹配，因此从s 的第二个字符之后继续匹配
            return self.isMatch(s, p[2:]) or \
                   first_match and self.isMatch(s[1:], p)
        else:
            # 第二个字符不是* 那么
            return first_match and self.isMatch(s[1:], p[1:])

    # 虽然递归表示很简单，但是这种题无脑肯定选择动态规划解
    def isMatch_(self, s: str, p: str) -> bool:
        pass