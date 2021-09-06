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

提示：

1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    # 1. 统计该字符串中需要最少删除多少个左右括号才能保证有效。
    def get_remove_num(self, s: str):
        left, right = 0, 0
        for c in s:
            if c == "(":
                left += 1
            if c == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

    # 2. 判断字符串是否合法有效。
    def is_valid(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    # 3. 回溯方法
    def removeInvalidParentheses(self, s: str):
        # 先判断有多少字符是不合法的 左括号和右括号
        rm_left, rm_right = self.get_remove_num(s)
        ans = []
        def dfs(left: int, right: int, start: int, ss: str):
            # 当删除了所有左括号和右括号的不合法数量时，如果剩余的字符是合法的，加入最终结果
            if left == right == 0 and self.is_valid(ss):
                ans.append(ss)

            for i in range(start, len(ss)):
                c = ss[i]
                # 去重复 当出现连续的左括号或者右括号时，无论删除哪一个都行
                if i > 0 and ss[i] == ss[i-1]:
                    continue
                # 当遍历到当前字符为左括号时，并且左括号的异常数量大于0，说明需要删除左括号
                if c == "(" and left > 0:
                    # 删除左括号，数量减1，因为原始i的位置为左括号，因此删除之后起始点还是从i开始，
                    dfs(left - 1, right, i, ss[:i] + ss[i + 1:])
                # 当遍历到当前字符为右括号时，并且右括号的异常数量大于0，说明需要删除右括号
                elif c == ")" and right > 0:
                    dfs(left, right - 1, i, ss[:i] + ss[i + 1:])
                # 当左右括号的数量都正常时，说明都必须要保留，直接判断下一个字符
        dfs(rm_left, rm_right, 0, s)
        return ans
