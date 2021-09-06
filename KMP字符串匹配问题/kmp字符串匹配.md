两个字符串匹配
~~~
主串A：      ababacba  (字符长度为m)
待匹配的串B： abac       (字符长度为n)

正常情况是循环
 for i in range(len(A)):
    以i为起始的位置后续是否与B是一致的。 遍历一遍 O(m)
    if A[i+len(B)] == B
    如果不等的话则从 i+1 重新匹配判断
此处的点是每次判断 A[i+len(B)] == B？ 得遍历一遍 O(n)
因此复杂度是 O(mn)
~~~
~~~
然而实际上在判断
A[i+len(B)] == B 是否相等时，如果不相等，可以不用从i+1 重新开始判断，即：
如果
   if A[i+len(B)] != B:
    下一次判断可以从 B 的前缀和后缀 相同字符串处开始。实际的
原算法
第一轮判断
     A:aba b acba
     B:aba c
第二轮判断
     A:aba b acba
     B: aba c
KMP算法
第一轮判断
     A:aba b acba
     B:aba c
第二轮判断
     A: aba b acba
     B:  aba c 本应当从i==2处继续往后
     B':  a bac 但是记录前缀和后缀公共字符{a} 因此已经判断的 aba 共有字符a，此时可以从B串a 之后的一个串开始匹配。