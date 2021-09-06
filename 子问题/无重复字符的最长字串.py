'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        s = list(s)
        n = len(s)
        if n==0:
            return 0
        maxlen = 1
        i = 0
        j =1
        dp[s[i]] = i
        while j<n:
            if s[j] not in dp:
                dp[s[j]] = j
                maxlen = max(maxlen, j-i+1)
            else:
                maxlen = max(j-dp[s[j]], maxlen)
                i = dp[s[j]]+1
                dp2 = dp.copy()
                for num in dp2:
                    if dp[num] < i:
                        dp.pop(num)
                dp[s[j]] = j
            j+=1
        print(maxlen)
        return maxlen
a = Solution()
s ="abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = 'abba'
a.lengthOfLongestSubstring(s)