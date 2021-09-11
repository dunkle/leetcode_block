'''
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。
示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]
 

示例 1：

输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：

输入：s = ")("
输出：[""]
 

提示：

1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def removeInvalidParentheses(self, s: str):
        '''
        括号问题，有效括号匹配分为两种匹配方式
        给定两个指针 leftcount righcount 记录遍历时左右两个括号的数量
        1、当遍历到左括号， leftcounnt +=1
        2、当遍历到右括号时， 如果左括号的数量大于0，即leftcount>0,那么 leftcount-=1
            否则 rightcount+=1
        依次遍历结束，leftcount 和 rightcount 的数目就是两者左括号和右括号要删除的数目
        :param s:
        :return:
        '''
        results = []
        n = len(s)
        if len(s)<2:
            return results
        leftcount, rightcount = 0, 0

        for i in range(n):
            if s[i]=='(':
                leftcount+=1
            elif s[i]==')':
                if leftcount==0:
                    rightcount+=1
                else:
                    leftcount-=1
            else:
                continue
        valstr = ''
        def dfs(s, index, leftcount, rightcount, valstr):
            if index==len(s):
                return
            if s[index]=='(':
                if leftcount!=0:
                    dfs(s, index+1, leftcount-1, rightcount, valstr)
                else:
                    valstr+=s[index]
            elif s[index]==")":
                if rightcount!=0:
                    dfs(s, index+1, leftcount, rightcount-1, valstr)
                else:
                    valstr+=s[index]
            else:
                valstr+=s[index]


            pass