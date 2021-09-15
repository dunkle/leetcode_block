def recur():
    b= 10
    def test():
        global b
        a = 5
        b = min(b, a)
        # print(b)
        print(a)
    test()
recur()
print(b)