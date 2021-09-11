'''
对于一个给定的字符串数组，请找到一种拼接顺序，使所有小字符串拼接成的大字符串是所有可能的拼接中字典序最小的。

给定一个字符串数组strs，同时给定它的大小，请返回拼接成的串。

测试样例：

["abc","de"],2
"abcde"
'''
class Solution:
    def largestMerge(self, arr):
        def compare_word(word1, word2):
            A = word1+word2
            B = word2+word1
            for i in range(len(A)):
                if A[i]>B[i]:
                    return True
                elif A[i]<B[i]:
                    return False
        #冒泡排序 交换
        n = len(arr)-1
        for j in range(n, 0,-1):
            for i in range(j):
                if compare_word(arr[i], arr[i+1]):
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        print(arr)

a = Solution()
arr = ["abc","de", 'a']
a.largestMerge(arr)
