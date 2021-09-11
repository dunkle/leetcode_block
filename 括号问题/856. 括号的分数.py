'''
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 

示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6
 

提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 有注释：
def scoreOfParentheses(s):
    '''

    :param s:
    :return:
    '''
    # 遇到 '(' 就加一个0 起占位作用 之后通过计算会变成 ..() 对应的分数
    stack = []
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(0)
        # 如果下一个是 ) 且匹配为最内层 '()' 则 0->1
        elif s[i]==')' and s[i-1]=='(':
            stack[-1] = 1
        # 如果下一个是 ')'形如 '))' 则持续pop 直到stack[-1]=0 这个0对应着最近的左括号
        # 此时该左括号对应的分数是 (...) 之间所有的数字加起来*2
        elif s[i]==')' and s[i-1]==')':
            inner = 0
            while stack[-1]!=0:
                inner+=stack.pop()
            stack[-1] = 2*inner
        print('i={} s[i]={} stack={}'.format(i, s[i], stack))
    # 此时不返回 stack[0] 而是stack之和 因为可能没有一个大的(..)包在其他括号外面
    # 例如s='()()' 那么我们遍历完之后是[1,1] 符合定义 但是最后需要求和
    return sum(stack)
s = "(())"
a = scoreOfParentheses(s)
