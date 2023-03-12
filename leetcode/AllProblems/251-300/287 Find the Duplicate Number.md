# 287. Find the Duplicate Number

![image-20200404193150564](../../../.assert/image-20200404193150564.png)

给定一个长度为n+1的数组，内容为[1,n]范围内的数，其中只有一个数重复了，重复的次数大于等于1，求这个数。

## 排序法

首先将数组排序，然后遍历数组找到重复的值即可。

~~~python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
~~~

时间复杂度为O(NlogN)，空间复杂度为O(1)

## 判圈法

假设该数组表示的是一个链表， 数组的内容为下一个节点的位置，则根据题意该链表中一定有环，环是由两个重复元素构成的，因为处在不同位置处两个相同元素的下一个坐标是相同的，因此环的起点即为这个歌重复元素。只要找到环的起点即可。

使用Floyd判圈法找到环起点的方法是：

1. 一快一慢两个指针在链表上运动，相遇后暂停
2. 将快指针放到链表头，并将步长改为和慢指针相同，则二者再一次相遇即为环头。

证明：

设链表头到环的距离为m，第一次相遇时所处位置距离环头长度为n，环的长度为S,快指针的步长是慢指针的2倍，则第一次相遇满指针走了$m+n$, 快指针走了$2(m+n)$或$m+n+kS$,k为整数，则$m+k=n$为S的整数倍。

第二次遍历时，快慢指针都走了m步，其中慢指针从m+n开始走的，而m+n为S的整数倍，因此二者第二次相遇一定是环的起始点。

![image-20200404194847233](../../../.assert/image-20200404194847233.png)

~~~python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
~~~

## 二分法

假设总长度为n，统计[1,n//2],[n//2,n]的个数，如果个数大于数组范围，那么说明有重复数组。

如[3,1,3,4,2]，先统计1-2,共出现2次，3-4出现3次，那么重复数组一定在3-4之间，下面统计3和4的个数即可。

注：二分法中mid是向下取整的，因此将mid划分到左边。

~~~python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        
        left, right = 1, n
        
        while left < right:
            mid = (left + right)//2
            lnum, rnum = 0, 0
            for num in nums:
                if left <= num <= mid:
                    lnum += 1
            if left == right and lnum > 1:
                return left
            if lnum > mid - left + 1:
                right = mid
            else:
                left = mid + 1
                    
        return left
~~~

时间复杂度分析：

二分法所用的时间为$O(logn)$,二分法中每一步需要遍历一次数组，时间为$O(n)$，因此最终时间复杂度为$O(nlogn)$

## 遍历法

由于数组元素值一定在数组长度内，因此直接与值对应的下标交换，如果下标位置已经有了，那么一定是重复的数组。

注：**这样会修改原来的数组**

~~~python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            while nums[i] == nums[nums[i]]:
                i += 1
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
~~~

