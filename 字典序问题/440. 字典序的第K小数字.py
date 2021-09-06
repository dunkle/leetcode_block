class Solution:
    def findKthNumber(self, n, k) -> int:
        '''
        以数字 i 开头的所有数字串 按字典序一定 排在以数字 i+1 开头的所有数字串的前面。
        对每个数字 i，唯一能做的就是确定以数字 i 开头的字符串的个数。
        但是有一个限制是，以 i 开头的数字不能超过最大数字 nn。
        :param n:
        :param k:
        :return:
        '''
        cur = 1
        prefix = 1

        while cur < k:
            cnt = self.get_count(prefix, n)  # 以数字i开始的数字个数
            if cur + cnt > k:
                # 说明以数字i开头的数字串太多了，并且第k个数字一定是以数字i开头。
                # 此时数字i更新为10*i，缩小搜索范围。
                # 位置p向前移动一位，因为新数字i字典序向后移动一位了
                prefix *= 10
                cur += 1
            else:
                # 说明将以数字i开头的数字串都算进去，也不够。
                #         说明数字i要增加到i+1。
                #         同时，位置p要跨过count个数字。
                prefix += 1
                cur += cnt
        # 此时prefix的位置就是
        return prefix
    def get_count(self, i, n):
        '''
        以数字i开头的字符 到小于n的字符有多少个
        :param i:
        :param n:
        :return:
        '''
        if i <= n:
            cnt = 1
        else:
            return 0
        a = i
        b = i + 1
        while True:
            a = a * 10
            b = b * 10
            if n >= b:
                cnt += b - a
            elif n >= a:
                cnt += n - a + 1
            else:
                break
        return cnt
