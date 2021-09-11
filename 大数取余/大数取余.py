# 求 (x^a) % p —— 循环求余法
def remainder(x, a, p):
    '''
    两个乘积之后 求余数 等于 分别求余数之后的乘积 再 求余
    (xy)⊙p=[(x⊙p)(y⊙p)]⊙p
    :param x:
    :param a:
    :param p:
    :return:
    '''
    rem = 1
    for _ in range(a):
        rem = (rem * x) % p
    return rem