![image-20210222204351446](../../../.assert/image-20210222204351446.png)

整体思路是求出这些直线所能构成的所有的直线，求出包含最多点的直线。

1. 没有必要求出所有的直线，对于点i，只需考虑i+1,l所能组成的直线即可。因为之前的直线已经在之前的点上计算过了。
2. 利用斜率判断两个点是否在同一直线上，由于计算机无法精确的表示整数，因此用两个值来表示斜率。为了确保不同点计算出的斜率一致，需要用最小公倍数对插值进行约分。

~~~python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 约分
        def frac(a, b):
            gcd = math.gcd(a, b)
            return a // gcd, b // gcd
        
        
        l, m = len(points), 0
        for i in range(l):
            slope_dict = {'i':1}
            same = 0
            for j in range(i+1, l):
                dx, dy = points[i][0]-points[j][0], points[i][1]-points[j][1]
                if dx < 0:
                    dx, dy = -dx, -dy
                slope = 0
                # 同一个点
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                # 斜率为无穷，也即垂直于y轴
                elif dx == 0:
                    slope = 'i'
                # 求斜率
                else:
                    slopex, slopey = frac(dx, dy)
                    slope = (slopex, slopey)
                if slope not in slope_dict:
                    slope_dict[slope] = 1
                slope_dict[slope] += 1
            if len(slope_dict) > 0:
                m = max(max(slope_dict.values())+same, m)
        return m
                    
                
~~~

