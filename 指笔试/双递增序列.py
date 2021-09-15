while True:
    try:
        nums1=[]
        nums2=[]
        num_list=input().split()
        for num in num_list:
            if num.isdigit():
                nums1.append(int(num))
            else:
                nums1.append(int(num[:-1]))
        num_list=input().split()
        for num in num_list:
            if num.isdigit():
                nums2.append(int(num))
            else:
                nums2.append(int(num[:-1]))

        if len(nums1)==0 or len(nums2)==0:
            print(0)
        else:
            def arr_fenpei(nums1, nums2):
                res1 = []
                res2 = []
                reslenth = 1
                # 两个递增序列，保证 (Si-S_(i-1)) = (Qi-Q_(i-1))对应相邻元素差相等
                # 因此两个序列第一个元素确定之后，采用贪心的方法，找对应差值匹配的即可
                for k in range(len(nums1)):
                    for t in range(len(nums2)):
                        i,j = k+1,t+1
                        res = 1
                        # 枚举两个序列 所有可能存在的作为第一个开始元素的值
                        xi = nums1[k]
                        xj = nums2[t]
                        list1 = [nums1[k]]
                        list2 = [nums2[t]]
                        while i<len(nums1) and j<len(nums2):
                            n1 = nums1[i]-xi
                            n2 = nums2[j]-xj
                            if n1>n2:
                                j+=1
                            elif n1<n2:
                                i+=1
                            else:
                                xi = nums1[i]
                                list1.append(nums1[i])
                                xj = nums2[j]
                                list2.append(nums2[j])
                                i+=1
                                j+=1
                                res+=1
                        if len(list1)>len(res1):
                            res1 = list1
                            res2 = list2
                            reslenth = max(reslenth, res)
                if reslenth!=1:
                    print(reslenth)
                    res1 = list(map(str,res1))
                    res2 = list(map(str,res2))
                    res1 = ' '.join(res1)
                    res2 = ' '.join(res2)
                    print(res1)
                    print(res2)
                if reslenth==1:
                    print(0)

            arr_fenpei(nums1,nums2)
        # print(nums1, nums1)
    except EOFError:
        break

'''
1 2 3 4 5
2 4 6 8

1 2 3 4 5 6 8 
2 4 6 8

1 2 3 4 5 7
2 4 6 8
'''