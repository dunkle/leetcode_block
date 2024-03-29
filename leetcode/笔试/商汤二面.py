class Solution:
    def singleNumber(self, nums):
        '''
        基于第一问的基础上，先异或一次，得到的数字是最后两个不同数字的异或值
        这个数字用二进制表示，必定有一位非0，即为1.
        10 和 15
        1010 异或 1101 -》 0111。以任意以为 为1的位作为标志分割位。（为了方便起见，选择第一次出现位      置为1 的位）

        nums中所有数字，只有两个只出现一次。把所有数字都用二进制位表示。
        以标志分割位作为标志位。 
        逐个判断数字，如果数字是0 ，分到第一组 A，如果数字是1，分到第二组B。
        因此，出现两次的数字，标志分割位无论是0还是1，肯定是被分为1组了。可能在A或者B
        但是只出现一次的数字，因为标志分割位，这两个数字不一样，因此被分别分在两个数组里。
        对第一组A 和第二组B分别 做异或，即可筛选出这两个数字。
        '''
        # 第一次异或获得两个数字的异或结果
        res = 0
        for i in nums:
            res^=i
        # 从最低位开始找，直到找到第一个不是0的位
        div=1
        while div&res==0:
            # 每次移位一位
            div<<=1
        a =0
        b = 0
        # 分别对两组 A、B进行异或
        for i in nums:
            if div&i:
                a^=i
            else:
                b^=i
        return [a,b]
            
        