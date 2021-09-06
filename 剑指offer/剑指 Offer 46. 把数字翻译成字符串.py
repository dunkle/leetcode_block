'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def translateNum(self, num: int) -> int:
        '''
        数字字母 在 10~25 之间 代表存在两位的可能性，等于两组求和
        dp[i] = dp[i−1]+dp[i−2] {10*Xi-1 + Xi  [10,25]  }
        如果数字为 单个位数，或者超过25 代表 只能一位
        dp[i] = dp[i−1]         {10*Xi-1 + Xi  (0,10)∪(25,99] }
​        :param num:
        :return:
        '''
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a