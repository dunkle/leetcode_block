class Solution:

    def rand10(self):
        """
        a = (rand(X)-1)Y + rand(Y) -> rand(1,X*Y)
        拒绝采样：
        要生成多少以内的数就 模多少 +1
        :rtype: int
        """
        def rand7():
            pass
        while True:
            a = rand7()
            b = rand7()
            c = (a-1)*7+b #(1,49)
            if c<=40:
                return c%10+1
            #继续优化
            #实际上生成了1~49之间的数字，但是只用了1~40
            # 对拒绝的9个数再次利用
            a2 = rand7() # 1~7
            b2 = c-40   #(1~9)
            c2 = (a2-1)*9 + b2 # (1~63)
            if c2<=60:
                return c2%10 + 1
