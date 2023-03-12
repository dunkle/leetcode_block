# 169. Majority Element

## 根据性质

众数是出现次数大于等于$n//2$次的数，那么对于数组中的一对数，如果二者不相等，则将其删除，最终留下的数一定为众数。

cand记录的是这对数的其中一个值，count记录该数出现的次数。遍历数组，若：

1. 值与cand相同，则count+1
2. 不同，
   1. 若count为0，说明之前不相同的数对已经删完了，找新的数对，cand=n,count=1
   2. count不为0，找到一个新的不相同数对，count-1

~~~python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, cand = 0, 0
        for n in nums:
            if n == cand:
                count += 1
            elif count == 0:
                cand, count = n, 1
            else:
                count -= 1
        return cand
~~~

## 分治法

将数组分成左右两个，分别求众数记作a,b

1. a == b则众数为a
2. 求ab中哪一个在数组中出现次数大于n//2

~~~python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a==b:
            return a
        return [b,a][nums.count(a) > len(nums)//2]
~~~

## 位操作

统计每一位出现的次数，如果次数大于n//2则保留，最终得到的就是原数的bit

~~~

~~~

## 排序法

~~~python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
~~~

