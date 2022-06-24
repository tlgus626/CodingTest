N = 5
A = [[10, 13, 10, 12, 15], [23, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]

apple = 0
s = e = N // 2

for i in range(N):
    for j in range(s, e + 1):
        apple += A[i][j]
    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(apple)
