class Solution:
    def characterReplacement(self, s, k):
        n = len(s)
        if n==0:
            return 0

        left, right = 0, 0
        max_len = 0
        dic = {}
        dic[s[0]] = 1
        for i in range(1, n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]] = 1
            lenth = i-left+1
            max_letter = max(dic, key=dic.get)
            print(max_len, max_letter)
            if dic[max_letter]+ k >= lenth:
                max_len = max(lenth, max_len)
                continue
            else:
                dic[s[left]]-=1
                left+=1
        return max_len

a =  Solution()
s = 'AABA'
len = a.characterReplacement(s, 2)
# s = "AABABBA"
# len = a.characterReplacement(s, 1)
print(len)