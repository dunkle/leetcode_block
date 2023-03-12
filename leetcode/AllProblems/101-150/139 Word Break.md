# 139. Word Break

![image-20200426142146829](../../../.assert/image-20200426142146829.png)

给定一个非空字符串和一个字典，判断字符串能否由字典中的单词组成。

## BFS

构造一个图，图的顶点为单词开始的字母，图的边为构成的单词。因此遍历这个字符串，将所有能构成字典中单词的index加入到queue中。

时间复杂度为$O(N^2)$



~~~python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = collections.deque()
        queue.appendleft(0)
        vis = set()
        vis.add(0)
        while len(queue) > 0:
            start = queue.pop()
            for i in range(start, len(s)+1):
                if i in vis:
                    continue
                if s[start:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    vis.add(i)
        return False
~~~

## 动态规划

设置数组dp，dp[i]表示i之前的所有数组都可以由单词构成，则：
$$
\text{dp}(i) = \begin{cases}
& True \quad \text{if} dp[i-l] \text{and} s[i-l:i] \text{in dict} \\
& \text{False}, \text{otherwise}
\end{cases}
$$
l为某一个单词的长度

~~~python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
        return dp[-1]
~~~

时间复杂度仍为$O(N^2)$