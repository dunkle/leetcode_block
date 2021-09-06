'''
698. 划分为k个相等的子集
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。


提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
'''
class Solution:
    def canPartitionKSubsets(nums, k):
        '''

        :param k:
        :return:
        '''
        if k==1: return True
        target, resid = sum(nums)//k, sum(nums)%k
        # 数字之后不能整除k，直接返回false，不能平分
        if resid!=0:
            return False
        def dfs(groups):
            if not nums:
                return True
            # [前进尝试] 选择数字 看放在哪个篮子里面 for i in range(k)
            now = nums.pop()
            for i in range(k):
                # 如果当前篮子的总和 加上 新加入的数字小于目标值，则放入该篮子
                groups[i]+=now
                if groups[i]<=target:
                    # [前进尝试]
                    # 放入篮子之后递归调用，剩下的数字继续往下是否可以放入篮子
                    if dfs(groups):
                        return True
                # [后退重置] gorups[i]返回状态
                # 当前篮子已经满了，放入该篮子不符合条件，考虑放在下一个篮子里
                groups[i]-=now

                # 如果篮子为空，直接放置该数字
                if groups[i]==0: break # 细节：减少重复搜索 保证0(没有数的篮子)始终在末尾
            # [后退重置] 循环所有的group之后 nums再返回之前状态，表示都无法放入篮子
            nums.append(now)
            return False
        nums = sorted(nums)
        # 如果最大值大于target则一定不能分成 -> 剪枝
        if nums[-1]>target:
            return False
        # 如果有等于target的单个数字 则将其先进行处理 -》 剪枝
        while nums and nums[-1]==target:
            nums.pop()
            # 篮子数量减1
            k-=1
        # 除去等于target的值，如果剩下的全是0说明篮子被用完了，即使剩下了0，也可以随机分配
        # 这一步往上对应着的是篮子可以被平分为这几个数 -》 剪枝
        # if not any(nums): return True
        if k==0: return True
        return dfs([0]*k)
