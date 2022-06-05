import sys

sys.stdin = open('input.txt', 'r')


def DFS(X, Y):
    global cnt
    if X == EX and Y == EY:
        cnt += 1
    else:
        for i in range(4):
            newX = X + dx[i]
            newY = Y + dy[i]
            # 새로 이동해야 할 곳이 아래 조건을 만족해야 이동함
            if 0 <= newX < N and 0 <= newY < N and A[X][Y] < A[newX][newY] and check[newX][newY] == 0:
                check[newX][newY] = 1  # 한번 방문하면 다시 방문 안하기 위해서
                DFS(newX, newY)
                check[newX][newY] = 0  # 새로운 루트를 짜야하니까 초기화


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    MIN = float('inf')
    SX = SY = 0
    MAX = -float('inf')
    EX = EY = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] < MIN:
                MIN = A[i][j]
                SX = i
                SY = j
            elif A[i][j] > MAX:
                MAX = A[i][j]
                EX = i
                EY = j
    check = [[0] * N for _ in range(N)]
    # initialize
    check[SX][SY] = 1
    DFS(SX, SY)

    print(cnt)
