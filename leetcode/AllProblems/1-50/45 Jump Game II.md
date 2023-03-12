

# 45. Jump Game II

![image-20210117202015701](../../../.assert/image-20210117202015701.png)

维护两个指针，分别表示当前可达到的下标范围，从中选一个最大的，直到达到最后一个数。

~~~python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        times = 1
        l, r = 0, nums[0]
        while r < len(nums)-1:
            nxt = max([i+nums[i] for i in range(l, r+1)])
            # 这里令l=r的原因是，假设nxt是通过[L,R]之间的m点到达的，那么m周围的点能到的距离一定小于nxt
            # 所以下一次只需判断[m, R]之间的即可
            l, r = r, nxt
            times += 1
        return times
    
~~~

