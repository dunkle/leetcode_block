'''
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        '''
        和被K整除的子数组 获得前缀和 P[j]-P[i] 代表子树组的和
        那么 (P[j]-P[i]) / K = 0 即两个整数 a,b相减对K能够整除，那么意味着 a 和b 对K的模余数相等（同余定理）
        只要 P[j] mod K == P[i] mod K
        :param A:
        :param K:
        :return:
        '''
        dic = {}
        dic[0] = 1
        acc, res = 0, 0
        for num in A:
            acc += num
            res += dic.get(acc%K,0)
            # 判断当前累积和对K的余数是否相等，同余定理。
            dic[acc%K] = dic.get(acc%K, 0) + 1
        return res
a = Solution()
A = [4,5,0,-2,-3,1]
K = 5
res = a.subarraysDivByK(A, K)
print(res)
