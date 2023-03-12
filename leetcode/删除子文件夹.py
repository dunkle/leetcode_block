folder = ["/a","/a/b","/c/d","/c/d/e","/c/f",'/']
print(sorted(folder))
folder = sorted(folder)
for i in range(len(folder)):
    folder.remove(folder[i])
    print(folder)
    print(folder[i])