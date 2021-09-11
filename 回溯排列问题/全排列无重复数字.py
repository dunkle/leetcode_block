class Solution:
    def permuteUnique(self, nums):
        res = []
        # 设置一个数组判断 元素是否已经被访问
        check = [0 for i in range(len(nums))]
        def recur(tmp, check):
            # print(tmp)
            # 终止条件就是加入tmp的元素和实际数组长度一致
            if len(tmp)==len(nums):
                # 需要存储copy，变量赋值和变量拷贝
                res.append(tmp.copy())
                return

            for i in range(len(nums)):
                if check[i]==1:
                    continue
                # 选择元素
                check[i] = 1
                tmp.append(nums[i])
                recur(tmp, check)
                #撤销选择
                tmp.pop()
                check[i] = 0
        recur([], check)
        return res