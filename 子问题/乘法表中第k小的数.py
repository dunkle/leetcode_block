'''
几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？

给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：

输入: m = 3, n = 3, k = 5
输出: 3
解释:
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
例 2：

输入: m = 2, n = 3, k = 6
输出: 6
解释:
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
注意：

m 和 n 的范围在 [1, 30000] 之间。
k 的范围在 [1, m * n] 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
    /*
    思路：二分法
    1、找第k小，第k大一类的问题，一般情况下都是用二分来解决，那么二分法就需要找到二分的数据点以及比较方式
    2、当前乘法表中最小值肯定是1，最大值为m*n，也就是我们这张表的最小和最大值，数据点找到
    3、比较方式，要找到第k小，那么我们在拿到mid数据点的时候，去看当前mid的位置，如果mid位置大于k，说明mid值太大，需要再次进行二分求解
    4、问题来了，这个位置怎么找呢，假设mid位于指定行i，那么mid/i也就是mid元素的列的位置，如果列的位置大于列最大长度n，那么说明该行所有数据都小于mid，累加n即可
       如果不是呢，说明找到了正确的行，只需要mid/i列的位置也就是这一行小于mid的元素个数
    5、边界条件的处理是二分法中比较重要的，我们要找第k小，那么可以理解为假设当mid处于某个值时，满足了条件，我们需要锁定大值，也就是count>=k，去调整l的值不断逼近
       当l的值逼近到某个数据，使得条件再次满足时，就是循环条件结束的时候，这样可以保证l的值一定是在原列表中的，因为+1或-1都会导致条件不满足
       当然我们的>=条件也是不允许的，因为满足之后l值就被锁定了
    */
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int):
        l = 1
        r = m*n
        while l<r:
            mid = (l+r)//2
            number = self.lessthanmid(m,n, mid)
            if number<k:
                l= mid+1
            else:
                r= mid
        return l
    def lessthanmid(self, m, n, num):
        count = 0
        for i in range(1, m+1):
            count += min(n, num//i)
        return count
a = Solution()
m = 1
n = 3
k = 2
minnum = a.findKthNumber(m ,n, k)
print(minnum)