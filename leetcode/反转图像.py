A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
k = len(A[0]) * [1]
f = list(map(lambda x, y: x ^ y, A[0], k))
print(f)
for i in range(len(A)):
    A[i] = map(lambda x, y: x ^ y, A[i][::-1], len(A[i])*[1])
