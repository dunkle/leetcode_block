# 4. Median of Two Sorted Arrays

给定两个已排序数组，求两个已排序数组的合并后的中位数。

## 暴力算法

合并两个有序数组，根据数组的大小，找到数组的中位数。

## 二分法

根据中位数的定义：

> **中位数**（又称**中值**，英语：Median），[统计学](https://zh.wikipedia.org/wiki/統計學)中的专业名词，代表一个样本、种群或[概率分布](https://zh.wikipedia.org/wiki/概率分布)中的一个数值，其可将数值集合划分为数量相等的上下两部分。对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。如果观察值有偶数个，则中位数不唯一，通常取最中间的两个数值的[平均数](https://zh.wikipedia.org/wiki/平均数)作为中位数。

我们要找到一个位置将一个数组切分成两部分，使左右两部分的元素数量相等。那么对于两个数组来说，我们可以分别在两个数组中找两个位置，使切分后两个数组左边元素数量的和和右遍元素数量的和相等，那么中位数就是左边的最大值和右遍最小值。

假设我们有A，B两个数组$A=[a_1, \dots, a_{i-1},a_i,\dots a_m]$，$B=[b_1,\dots b_{j-1},b_j,\dots, b_n]$，找到的切分位置为i和j。那么我们根据中位数的定义可以有如下结论：

1. $i+j = n-i + m-j$,也即$i+j = \frac{m+n}{2}$
2. $\max\{a_{i-1}, b_{j-1}\} \leq \min\{a_i, b_j\}$

也即我们只需找到一对$(i,j)$使i，j位置的元素满足上述关系即可。由第一个条件可知,$j = \frac{m+n}{2}-i$。也即我们只需遍历i的值，j由总长度推出即可。对于第二个条件，由于数组有序，那么已经有$a_{i-1}\leq a_i,b_{j-1}\leq b_j$，则只需满足$b_{j_i}\leq a_i,a_{i-1}\leq b_j$即可，继续观察$(i,j)$的关系可以得到，随着i的增大，j会不断减小，那么一定会有一个最大的i，使得$a_{i-1}\leq b_j$,由于i是最大的，那么一定有$a_i > b_j$，则$a_i > b_j > b_{j-1}$。

综上所述，我们只需在第一个数组中找到一个最大的i，满足$a_{i-1}\leq b_j$即可，此时中位数即为$\max\{a_{i-1}, b_{j-1}\}$（奇数）或$\max\{a_{i-1}, b_{j-1}\}$和$\min\{a_i, b_j\}$的平均数(偶数)，而在一个有序数组中查找一个元素，最快的方法就是二分查找，所以代码为：

~~~python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l, r, m, n = 0, len(nums1), len(nums1), len(nums2)
        m1, m2 = 0, 0
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            # 当在最后一个位置切分时，ai为正无穷，ai1为醉猴一个值。数组B同理
            am1 = -float('inf') if i == 0 else nums1[i-1]
            a = float('inf') if i == m else nums1[i]
            bm1 = -float('inf') if j == 0 else nums2[j-1]
            b = float('inf') if j == n else nums2[j]
            
            # 如果当前i为最大的，更新m1和m2后
            # l=i+1，则永远不会出现am1 > b的情况
            # 只会不断缩小r,使l>r,跳出循环
            if am1 <= b:
                m1, m2 = max(am1, bm1), min(a, b)
                l = i + 1
            else:
                r = i-1     
        return (m1 + m2) / 2 if (m+n)%2==0 else m1
~~~



