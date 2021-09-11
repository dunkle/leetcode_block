class Solution:
    def singleNumbers(self, nums):
        '''
        一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
        请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
        示例 1：
        输入：nums = [4,1,4,6]
        输出：[1,6] 或 [6,1]
        示例 2：

        输入：nums = [1,2,10,4,1,4,3,3]
        输出：[2,10] 或 [10,2]
         

        限制：

        2 <= nums.length <= 10000

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :param nums:
        :return:
        '''
        m = len(nums)
        res = 0
        # 第一遍异或，得到两个不同数字的异或值
        for i in range(m):
            res ^=nums[i]
        flag = 1
        # 找出第一个1，代表了标志位，两个数字在该位不同的值
        while True:
            if res&flag:
                break
            else:
                flag<<=1
        a = 0
        b = 0
        # 依据标志位将数字分为两组，两个不同的数字必定被分为两组
        for i in range(m):
            if flag&nums[i]:
                a^=nums[i]
            else:
                b^=nums[i]
        return [a, b]

a = Solution()
nums = [1,2,5,2]
res = a.singleNumbers(nums)
print(res)