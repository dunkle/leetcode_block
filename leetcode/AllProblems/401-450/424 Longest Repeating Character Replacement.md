给定一个字符串，可以将其中一个字符变为任意一个大写字母，最多可以操作K次，求操作之后最长的重复子串。



使用滑动窗口，滑动窗口的一般思路是：

1. 滑动右指针，找到一个满足条件的窗口
2. 滑动左指针，进行收缩
3. 重复1-2，知道右指针到达边界

在本题中，首先如何找到一个符合条件的窗口。首先看一下一个符合条件的窗口满足什么性质：

1. 一个满足条件的窗口，不被替换的元素一定是出现次数最多的元素,假设出现次数为f
2. 则被替换元素的数量为l-f，其中l为当前窗口的大小
3. 根据题意，如果该窗口满足条件，则k >= l-f

所以解题的关键是判断当前窗口满足条件的依据是k>=l-f

那么该题的解决方法是：

1. 滑动右指针，更新每个字符出现的次数
2. 如果找到一个满足条件的窗口，更新答案
3. 不满足时滑动左指针

~~~python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        # maxf,maxc保存出现次数最多的字符及其出现的次数
        maxf, maxc = 0, 'A'
        result = 0
        counter = Counter()
        
        while r < len(s):
            counter[s[r]] += 1
            if maxf < counter[s[r]]:
                maxf = counter[s[r]]
                maxc = s[r]
            # 如果满足条件则更新result
            if maxf+k >= r-l+1:
                result = max(result, r-l+1)
            else: # 不满足是更新左指针
                if s[l] == maxc:
                    maxf -= 1
                counter[s[l]]-=1
                l+=1
            r += 1
        return result
~~~

