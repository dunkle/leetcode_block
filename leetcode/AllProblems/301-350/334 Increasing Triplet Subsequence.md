# 334. Increasing Triplet Subsequence

![image-20200426144145152](../../../.assert/image-20200426144145152.png)

判断一个数组中是否存在三个递增的数。

找到第一个和第二个最小的数，找到一个比他大的即可。

~~~python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
~~~



