import sys

sys.stdin = open('input.txt', 'r')


def DFS(X, Y):
    global cnt
    if X == 6 and Y == 6 :
        cnt += 1
    else:
        for i in range(4) :
            newX = X+dx[i]
            newY = Y+dy[i]
            # 새로 이동해야 할 곳이 아래 조건을 만족해야 이동함
            if 0<=newX<=6 and 0<=newY<=6 and A[newX][newY] == 0 :
                A[newX][newY] = 1 # 한번 방문하면 다시 방문 안하기 위해서
                DFS(newX, newY)
                A[newX][newY] = 0 # 새로운 루트를 짜야하니까 초기화

if __name__ == '__main__':
    A = [list(map(int, input().split())) for _ in range(7)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    A[0][0] = 1 # initialize
    DFS(0, 0)
    print(cnt)