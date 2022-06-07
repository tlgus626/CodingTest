import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 6)  # 재귀함수 제한시간 설정


# 모든 출발지를 탐색하는 건 비효율적이야
# 10번째 행에서 목적지(2)에서 출발해서 역으로 사다리를 탄 뒤, 도착지 열 정보를 출력하는 게 효율적!!

def DFS(x, y):
    check[x][y] = 1
    if x == 0:
        print(y)
    else:
        # 갈 수 있는 방향 확인
        if y - 1 >= 0 and A[x][y - 1] == 1 and check[x][y - 1] == 0:
            DFS(x, y - 1)
        elif y + 1 < 10 and A[x][y + 1] == 1 and check[x][y + 1] == 0:
            DFS(x, y + 1)
        else:
            DFS(x - 1, y)


if __name__ == '__main__':
    A = [list(map(int, input().split())) for _ in range(10)]
    check = [[0] * 10 for _ in range(10)]
    for i in range(10):
        if A[9][i] == 2:
            DFS(9, i)
