# 78. Subsets

![image-20200804111528009](../../../.assert/image-20200804111528009.png)

给一个集合求所有的子集

## bitmask方法

用一个二进制数中的0，1来决定是否选择对应位上的数字，比如集合[1,2,3]，二进制数为001，则对应的子集为[3]。

使用这种方法代码量是最少的，但是问题在于能否正确的生成bitmask，也即如何生成正确的前导零。python中使用的方法是，生成一个n+1位的数，利用后面的n位：

~~~python
for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    bitmask = bin(i)[3:]
~~~

python中bin方法生成的是一个以0b开头的字符串，代表这个数的二进制。

~~~python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        # 处理前导零
        for i in range(2**n, 2**(n+1)):
            print(bin(i))
            bitmask = bin(i)[3:]
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            
        return ans
~~~

时间复杂度分析为$O(N2^N)$，共有$2^N$个子集，其中每个子集需要遍历长度为$N$的mask