import sys

sys.stdin = open('input.txt', 'r')

# 최단 거리 : (0,0)에서 (N-1,N-1)로 오른쪽 or 아래로 이동함 i.e., A[i][j]는 왼쪽 or 위에서 내려옴

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# dynamic table : 출발 지점에서 dy[i][j]까지 오는 데 필요한 최소 비용
# for memoization
dy = [[0] * N for _ in range(N)]


# top down
def DFS(x, y):
    # cut edge
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return A[0][0]
    else:
        if y == 0:  # 0열이 됨
            dy[x][y] = DFS(x - 1, y) + A[x][y]
        elif x == 0:  # 0행이 됨
            dy[x][y] = DFS(x, y - 1) + A[x][y]
        else:
            dy[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + A[x][y]
        return dy[x][y]


print(DFS(N - 1, N - 1))
