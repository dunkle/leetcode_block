# 525. Contiguous Array

![image-20200413192945925](../../.assert/image-20200413192945925.png)

给定一个0，1数组，找到最长的0，1子数组的长度。

## 暴力

~~~python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            nzeros = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    nzeros += 1
                else:
                    nzeros -= 1
                if nzeros == 0:
                    max_len = max(max_len, j-i+1)
        return max_len
~~~

时间复杂度为$O(N^2)$,空间复杂度为$O(1)$

## 使用额外空间

使用一个Count变量记录当前遇到的0，1对，遇到0就加1，遇到1减1。则当Count为0时，从数组开始到当前位置，01的数量是相等的。还有就是当Count的数量重复时，与上次一次这个Count位置之间的0，1是相等的。如下图所示：

![image-20200413193423579](../../.assert/image-20200413193423579.png)

其中[A,B],[B,C],[A,C]之间的0，1数量是相同的。Count值得范围是[-n,n]，因此创建一个2n+1的数组A，数组下标为Count的值，初始化为-2，A[0]=-1。每当$A[Count]\neq-2$时，根据最早的count更新max_len

~~~python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_array = [-2]*(2*len(nums)+1)
        count_array[0] = -1
        count, max_len = 0, 0
        for i, n in enumerate(nums):
            if n == 0:
                count += 1
            else:
                count += -1
            if count_array[count] > -2:
                max_len = max(i-count_array[count], max_len)  
            else:
                count_array[count] = i
        return max_len
~~~

时间复杂度为$O(N)$,空间复杂度为$O(N)$

## HashMap

使用hashmap记录遇到的Count而不用额外的数组。

~~~python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_dict = {0:-1}
        count, max_len = 0, 0
        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            if count in count_dict:
                max_len = max(max_len, i-count_dict[count])
            else:
                count_dict[count] = i
        return max_len
~~~

时间复杂度为$O(N)$,空间复杂度为$O(N)$