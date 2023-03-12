# 结果返回字符串
# 10 20

# 100位以内 0~9之内
def mul(num1, num2):
    # 排除 num1 num2 中为0 直接返回0
    if num1=='0' or num2=='0':
        return '0'
    len1 = len(num1)
    len2 = len(num2)
    # 两数乘积最长
    ans = [0]*(len1+len2)
    # 从前往后
    for i in range(0,len1):
        a = int(num1[i])
        for j in range(0, len2):
            b = int(num2[i])
            tmp = a*b
            ans[i+j+1] = tmp
    # print(ans)
    for i in range(len(ans)-1, -1,-1):
        # 进位
        ans[i-1] += ans[i]//10
        # 余数
        ans[i] = ans[i]%10
    # print(''.join(str(x) for x in ans))
    if ans[0]==0:
        ans = ans[1:]
    res = ''.join(str(x) for x in ans)
    return res

num1 = '10'
num2 = '20'
num1 = '24'
num2 = '24'

# num2 = '30'
# num2 = '0'
res = mul(num1, num2)
print(res)