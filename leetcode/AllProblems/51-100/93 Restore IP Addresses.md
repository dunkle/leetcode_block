![image-20201008163842975](../../../.assert/image-20201008163842975.png)

给定一段字符串，求出所有能组成合法ip的数量

1. 找到四个切分点，切分点之间字符串的长度为[1,3]
2. 判断切分点之间的数字是否符合ip的定义
3. 去除包含前导零的情况

~~~python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        # 防止解析字符串出错，判断a+b+c+d是否为原字符串长度
                        if a+b+c+d != len(s):
                            continue
                        # 由于a,b,c,d都是1-3，因此注意切分字符串时的起始位置
                        A, B, C, D = int(s[:a]), int(s[a:a+b]), int(s[a+b:a+b+c]), int(s[a+b+c:a+b+c+d])
                        if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                            ip = "{}.{}.{}.{}".format(A,B,C,D)
                            # 为了防止有前导零，判断加上.之后与原字符串的长度是否相同
                            if len(ip) == (len(s)+3):
                                result.append(ip)
        return result
~~~

