import sys

sys.stdin = open('input.txt', 'r')

# 최단 거리 : (0,0)에서 (N-1,N-1)로 오른쪽 or 아래로 이동함 i.e., A[i][j]는 왼쪽 or 위에서 내려옴

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# dynamic table : 출발 지점에서 dy[i][j]까지 오는 데 필요한 최소 비용
dy = [[0] * N for _ in range(N)]

# initialize (0행, 0열)
dy[0][0] = A[0][0]
for i in range(N):
    dy[0][i] = dy[0][i - 1] + A[0][i]  # 0행은 오른쪽으로 가는 경로만 가능
    dy[i][0] = dy[i - 1][0] + A[i][0]  # 0열은 아래로 가는 경로만 가능

# dynamic programming
for i in range(1, N):
    for j in range(1, N):
        dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + A[i][j]

print(dy[N - 1][N - 1])
