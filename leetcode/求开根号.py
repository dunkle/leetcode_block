n = 100
a = 1
# print(a)
while abs(a*a-n)>=0.01:
    # f(x)函数 a^2 -n,n为待逼近的数
    # x^2 的一阶导 2x,a初始化为1
    a =a - (a*a-n)/(2*a)
print(a)

def mySqrt(x: int) -> int:
    if x==0:
        return 0
    x0 = 1
    while abs(x0*x0-x)>=1:
        x0 = x0-(x0*x0-x)/(2*x0)
    return int(x0)
res = mySqrt(n)
print(res)