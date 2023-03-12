给定一个无序数组，找到第一个不存在的正整数。

1. 对于一个长度为l的数组，第一个不存在的正整数必在[1,...,l+1]中
2. 对于不在这个范围内的数字可以忽略
3. 将整个数组看作是一个hashtable，用下标记录该范围内的数出现的频率
4. 为了不破坏存放在原始位置的数的大小，因此采用+n的方式及取余的方式记录频率

~~~python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i]%n] += n
            
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        
        return n
~~~

