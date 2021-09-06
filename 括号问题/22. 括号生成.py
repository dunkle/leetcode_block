'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def generateParenthesis(self, n: int):
        '''
        生成有效的括号，给定了数字，说明左括号和右括号数量初始都是n
        需要遵循先放左括号再放右括号
        :param n:
        :return:
        '''
        result = []
        if n==0:
            return result
        elif n==1:
            result.append("()")
        else:
            def recur(s,l,r):
                # 当没有左括号了，只能放右括号，全部放下，存结果
                if l==0:
                    s+=r*')'
                    result.append(s)
                    return
                else:
                    # 当放下的左括号的数量大于右括号时，此时可以继续放左括号或者放右括号
                    if l<r:
                        recur(s+'(',l-1,r)
                        recur(s+')',l,r-1)
                    # 当放下的括号里左括号少于等于右括号，说明此时只能放左括号
                    else:
                        recur(s+'(',l-1,r)
            recur('(',n-1,n)
        return result
