class Solution:
    def permuteUnique(self, nums):
        '''
        时间复杂度：O(N*N!)。
        空间复杂度：O(N)
        :param nums:
        :return:
        '''
        res = []
        #需要先排序，方便后续去重
        nums = sorted(nums)
        check = [0 for i in range(len(nums))]
        def recur(tmp, check):
            if len(tmp)==len(nums):
                res.append(tmp.copy())
                return
            for i in range(len(nums)):
                if check[i]==1:
                    continue
                # 可以优化的点在
                # if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0
                # 找check[i]为0的点避免一直找1
                # i>0 的判别条件，保证至少有一个元素，i-1>0,去重
                if i>0 and nums[i]==nums[i-1] and check[i-1]==1:
                    continue
                check[i]=1
                tmp.append(nums[i])
                recur(tmp, check)
                check[i]=0
                tmp.pop()
        recur([], check)
        return res