'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dictmap = {}
        allnum = len(t)
        for i in t:
            if i in dictmap:
                dictmap[i] += 1
            else:
                dictmap[i] = 1
        # print(dictmap)
        i, j = 0, 0
        m = len(s)
        dict_ = dictmap.copy()
        minlen = float('inf')
        res = ''
        while j < m:
            if s[j] in dictmap:
                if dict_[s[j]]:
                    dict_[s[j]] -= 1
                    allnum -= 1
            if allnum == 0:
                while i < j:
                    print(dictmap, dict_)
                    if s[i] in dictmap and dict_[s[i]] == 0:
                        if minlen<j-i+1:
                            res = s[i:j]
                        minlen = min(minlen, j - i + 1)
                        dict_[s[i]] += 1
                        allnum += 1
                        i += 1
                        break
                    i = i + 1
            j += 1
        print("lenth", minlen, res)

    def minWindow1(self, s, t):
        # 从s中找到包含t的所有字符
        # 1、先对t建立一个hash表记录每个字符的个数
        # 2、设置一个左右指针 i,j，先滑动j直到i，j区间包含所有t字符，也就是hash表对应元素值都为0
        # 3、当hash表中所有字符都为0之后（需要判断），收缩左边界i，把多余字符去掉，计算最短区间
        # 3-1 判断所有字符是否为0，可以设置一个计算总数字符是否为0的变量，优化，遍历一遍字典查找
        # 4、达到最短区间之后，i继续+1 ，对应hash表中字符+1，此时所有字符不为0 重复2
        # 5、直到j超出右边界
        from collections import defaultdict
        hashdict = defaultdict(int)
        allnum = len(t)
        for i in range(len(t)):
            hashdict[t[i]] += 1
        print(hashdict)
        i, j = 0, 0
        n = len(s)
        minlenth = n
        res = ''
        while j<n:
            if allnum==0:
                while s[i] not in hashdict or hashdict[s[i]]<0:
                    i+=1
                if j-i+1<minlenth:
                    res = s[i:j]
                minlenth = min(j-i+1, minlenth)
                hashdict[s[i]]+=1
                i+=1
                allnum+=1
                j+=1
            if s[j] in hashdict:
                if hashdict[s[j]]>0:
                    allnum-=1
                hashdict[s[j]]-=1
            j+=1

        return res




a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
a.minWindow(s, t)
res = a.minWindow1(s, t)
print(res)
