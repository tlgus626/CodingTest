import sys

sys.stdin = open('input.txt', 'r')


def DFS(X, Y):
    global cnt
    # 집 하나를 발견한거니까 +1
    cnt += 1
    # 추가로 방문하지 않기 위해 0으로 바꿔두기
    A[X][Y] = 0
    for i in range(4):
        newX = X + dx[i]
        newY = Y + dy[i]
        if 0 <= newX < N and 0 <= newY < N and A[newX][newY] == 1:
            DFS(newX, newY)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = list()
    # initialize
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                # 매 새로운 단지를 발견할 때마다 cnt=0으로 초기화
                cnt = 0
                # 그 집에서부터 인접한 집 찾기 시작
                DFS(i, j)
                # 해당 단지 탐색 다 끝나면 집 개수를 리스트에 넣어주기
                res.append(cnt)
    print(len(res))
    for r in sorted(res):
        print(r)
