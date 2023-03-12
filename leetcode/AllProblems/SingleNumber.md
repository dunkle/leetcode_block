# Single Number Ⅰ

利用性质a^b^a = b

~~~python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = nums[0]
        for v in nums[1:]:
            t = t ^ v
        return t
~~~

# Single Number Ⅱ

## 哈希表

~~~python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = dict()
        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        for k, v in hash.items():
            if v == 1:
                return k
~~~



## 数学推算

对出现的所有数求和，和乘3之后减原始数据的和，对结果除2即可

~~~python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums)) // 2
~~~

# Single Number Ⅲ

## 位运算

首先根据xor运算，得到两个数之间位的差异，然后利用其中一位将数组分成两部分，分别进行xor运算，得到最终的两个数

~~~python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for n in nums[1:]:
            xor = xor ^ n
        mask = 1
        while mask&xor:
            mask = mask << 1
        a, b = 0, 0
        for n in nums:
            if n&mask:
                a^=n
            else:
                b^=n
        return [a, b]
~~~

