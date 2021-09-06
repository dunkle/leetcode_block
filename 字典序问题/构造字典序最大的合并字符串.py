class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        '''
        双指针，一个指针指向word1 一个指针指向word2 谁大选谁
        当两者相同的时候，一直往下找，直到出现不同的字符为止，谁大选谁，并且之前相同的也需要加入merge
        （需要考虑 指针是否指向word 的末尾了， 如果谁指向末尾了，就让对应的指针+1 继续往下判断
        :param word1:
        :param word2:
        :return:
        '''
        i, j = 0, 0
        n, m = len(word1), len(word2)
        ans = ''
        while i < n and j < m:
            if ord(word1[i]) > ord(word2[j]):
                ans += word1[i]
                i += 1
            elif ord(word1[i]) < ord(word2[j]):
                ans += word2[j]
                j += 1
            else:
                tempi = i
                tempj = j
                # 出现相同时一直往下找，保证找的同时不超出边界
                while tempj < m and tempi < n and ord(word1[tempi]) == ord(word2[tempj]):
                    tempi += 1
                    tempj += 1
                #终止条件一 其中一个word 或者两者都到达边界情况
                if (tempj == m) or (tempi == n):
                    # 当word1达到边界
                    if tempj == m:
                        ans += word1[i]
                        i += 1
                    else:
                        ans += word2[j]
                        j += 1
                # 当两者字符不相等， 判断哪个字符大选哪个
                else:
                    if ord(word1[tempi]) < ord(word2[tempj]):
                        ans += word2[j]
                        j += 1
                    else:
                        ans += word1[i]
                        i += 1
        # 当其中一个字符串到达边界时，另一个字符串需要把后续字符全部加上
        if i == n:
            ans += word2[j:]
        if j == m:
            ans += word1[i:]
        return ans

a = Solution()
word1 = "abcabc"
word2 = "abdcaba"
word1 = "cabaa"
word2 = "bcaaa"
res = a.largestMerge(word1, word2)
print(res)