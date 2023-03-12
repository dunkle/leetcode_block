a = [13, 12, 10, 1,0]
a = [3,30,34,5,9]

c = map(lambda i: str(i), a)
c =sorted(c)
def fil_(line):
    if line=='0':
        print("True")
        return False
    return True
e = filter(lambda i: i!='0', c)
d = ''.join(e)

print('e', list(e))
print('d', d)
