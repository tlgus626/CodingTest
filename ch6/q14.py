import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6) # 재귀함수 제한시간 설정

def DFS(X, Y, h):
    check[X][Y] = 1
    # 인접한 지역도 물에 안잠겼는지 확인
    for i in range(4):
        newX = X + dx[i]
        newY = Y + dy[i]
        # 인접한 지역 중, 물에 안잠긴 곳
        if 0 <= newX < N and 0 <= newY < N and check[newX][newY] == 0 and A[newX][newY] > h:
            DFS(newX, newY, h)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0  # 안전 영역이 몇 개인지?
    res = 0  # 최종 답 (최댓값 찾기)
    # 높이의 범위가 1~100이므로 : 높이가 0이면 안전 영역 1개, 높이가 100이면 안전 영역 0개
    # -> 높이가 100인 경우는 반복문 돌릴 필요 없음
    for h in range(100):
        # initialize
        check = [[0] * N for _ in range(N)]
        cnt = 0
        # 높이가 정해지면 이중 리스트 탐색 시작!
        for i in range(N):
            for j in range(N):
                # 물에 잠기지 않은 육지에 해당
                if check[i][j] == 0 and A[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        # 최댓값 찾기
        res = max(res, cnt)
        # 모든 지역이 물에 잠겼으므로 안전 영역 0개 = 더 이상 h를 높일 필요가 없음
        if cnt == 0:
            break
    print(res)