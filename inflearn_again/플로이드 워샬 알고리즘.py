N, M = 5, 8
XYD = [(1, 2, 6), (1, 3, 3), (3, 2, 2), (2, 4, 1),
       (2, 5, 13), (3, 4, 5), (4, 2, 3), (4, 5, 7)]

A = [[30] * N for _ in range(N)]
for i in range(N):
    A[i][i] = 0
for x, y, d in XYD:
    A[x - 1][y - 1] = d

# dynamic programming
for i in range(N):
    for j in range(N):
        for k in range(N):
            A[i][j] = min(A[i][j], A[i][k] + A[k][j])

# print
for i in range(N):
    for j in range(N):
        if A[i][j] == 30:
            print('M', end=' ')
        else:
            print(A[i][j], end=' ')
    print()
