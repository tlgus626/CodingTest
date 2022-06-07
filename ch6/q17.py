import sys

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10 ** 6)  # 재귀함수 제한시간 설정

def DFS(L, S):
    global MIN
    # 하나의 조합이 완성됨
    if L == M :
        # 도시의 피자거리
        dist = 0
        for j in range(len(house)) :
            hx = house[j][0]
            hy = house[j][1]
            hd = float('inf')
            # 선택된 피자집
            for c in combn :
                px = pizza[c][0]
                py = pizza[c][1]
                hd = min(hd, abs(hx-px)+abs(hy-py)) # 집 하나마다 최소 거리의 피자집이 정해짐
            # 각 집의 피자거리 합해주기
            dist += hd
        # 최소거리인지?
        if dist < MIN :
            MIN = dist
    else :
        for i in range(S, len(pizza)) :
            combn[L] = i
            DFS(L+1, i+1)

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    house = []
    pizza = []
    for i in range(N) :
        for j in range(N) :
            if A[i][j] == 1 :
                house.append((i,j))
            elif A[i][j] == 2 :
                pizza.append((i,j))
    # 조합의 경우의 수 = 살아남을 M개의 피자집
    combn = [0]*M
    # 최소거리
    MIN = float('inf')
    # DFS 시작
    DFS(0, 0)

    print(MIN)