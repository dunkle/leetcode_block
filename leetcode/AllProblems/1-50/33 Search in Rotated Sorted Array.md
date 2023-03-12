# 33. Search in Rotated Sorted Array

![image-20200420111459900](../../../.assert/image-20200420111459900.png)

给定一个旋转后的有序数组，利用二分查找找某一个值。

## 找最小值

最小值在中间部分，因此可以通过二分查找向中间靠拢，找出最小值，则最小值的位置即为旋转的次数。然后使用通用的二分查找，在判断mid时进行一次坐标转换即可。
$$
realmid = (mid+rottimes) \text{mod} len
$$

~~~python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (hi+lo)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        rot = lo
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) // 2
            realmid = (mid + rot)%len(nums)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                hi = mid-1
            else:
                lo = mid+1
        return -1
~~~

## 二分查找

将数组分成两部分，以最小值为界，左边比右边大。如[4,5,6,7,0,1,2].此时target和mid可能有两种情况：

1. 二者在同一边，直接使用通用的二分查找即可
2. 二者在两边，此时需要调整数组内容，为了使用通用的二分查找，需要把mid所在的区间设置比target所在的大或小，也即变为[4,5,6,7,INF,INF,INF]，或[-INF,-INF,-INF,-INF,0,1,2]即可使用二分查找。

如何判断在哪一边？

当mid和target都比array[0]大或小时，二者即在不同边。

如何判断设置INF或-INF

1. mid>target，说明mid在坐标，则设置为-INF
2. mid<target，说明在右边设置为INF

~~~python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            # print(lo, hi)
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            # 注意这里加括号，否则python会把它当成一个连等
            # 这里必须要与左边界比较，否则当数组没有旋转时，会丢失右边界
            if (nums[mid] >= nums[lo]) == (target >= nums[lo]): # same side
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] > target:
                    nums[mid] = -math.inf
                    lo = mid + 1
                else:
                    nums[mid] = math.inf
                    hi = mid -1
        return -1
~~~

