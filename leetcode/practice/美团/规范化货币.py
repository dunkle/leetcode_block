# encoding: utf-8
# ------------ 美团 ---------------
# 整数：要求每三位一个英文逗号
# 小数：全部两位，其余位数舍去（不四舍五入）
# 负数：数值两端加上英文括号，省略负号
# 在数值前面，括号后面（如果有括号），加上$
# 给定多行数据：无前导0，无-0，每个字符串长度不超过100
# 输入：
# 203323
# 0.0
# 0.000000
# 0.009212121
# 343444323.32432
# -12344.1
# -12345678.9
# 输出
# $203,323.00
# $0.00
# $0.00
# $0.00
# $343,444,323.32
# ($12,344.10)
# ($12,345,678.90)

# ---------- 正则化 + 字符串 -----------------
import re


# 整数部分每三位一个英文逗号
def comma(str):
    count = 0  # 循环计数
    sumstr = ''  # 待拼接的字符串
    for one_str in str[::-1]:  # 注意循环是倒着输出的
        count += 1  # 计数
        if count % 3 == 0 and count != len(str):  # 如果count等于3或3的倍数并且不等于总长度
            one_str = ',' + one_str  # 当前循环的字符串前面加逗号
        sumstr = one_str + sumstr  # 拼接当前字符串
    return sumstr  # 返回拼接的字符串


def main():
    while True:  # 循环输入
        data = input().strip()
        # ------ 正则表达式 ---------------
        re_neg_dec = r"-{1}\d+\.{1}\d+"
        re_neg_int = r"-{1}\d+"
        re_pos_dec = r"\d+\.{1}\d+"
        re_pos_int = r"\d+"

        # ----------- 正则匹配 -------------
        # ----------- -1.2 ---------------
        if re.match(re_neg_dec, data):
            part = data.split(".")
            partInt = comma(part[0][1:])
            if len(part[1]) == 1:
                partDec = part[1] + "0"
            else:
                partDec = part[1][:2]
            res = "($" + "".join(partInt) + "." + "".join(partDec) + ")"  # 字符串的连接

        # ----------- -1 ---------------
        elif re.match(re_neg_int, data):
            part = comma(data[1:])
            res = "($" + "".join(part) + ".00" + ")"
        # ---------- 1.2 ---------------
        elif re.match(re_pos_dec, data):
            part = data.split(".")
            partInt = comma(part[0])
            if len(part[1]) == 1:
                partDec = part[1] + "0"
            else:
                partDec = part[1][:2]
            res = "$" + "".join(partInt) + "." + "".join(partDec)  # 字符串的连接
        # ----------- 12 ---------------
        elif re.match(re_pos_int, data):
            part = comma(data)
            res = "$" + "".join(part) + ".00"
        else:
            res = ""

        print(res)


main()
