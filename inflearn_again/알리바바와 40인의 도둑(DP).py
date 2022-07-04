N = 5
A = [[3, 7, 2, 1, 9], [5, 8, 3, 9, 2], [5, 3, 1, 2, 3], [5, 4, 3, 2, 1], [1, 7, 5, 2, 4]]

dy = [[0] * N for _ in range(N)]

dy[0][0] = A[0][0]
for i in range(N):
    dy[0][i] = dy[0][i - 1] + A[0][i]
    dy[i][0] = dy[i - 1][0] + A[i][0]

for i in range(1, N):
    for j in range(1, N):
        dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + A[i][j]

print(dy[N - 1][N - 1])
