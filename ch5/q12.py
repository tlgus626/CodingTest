import sys

sys.stdin = open('input.txt', 'r')

# 그래프 : 노드와 간선의 집합
# 방향 그래프 : 간선의 방향이 설정되어있음
# 가중치 방향 그래프 : 간선마다 가중치가 설정되어있음

# 인접행렬 : 행에서 열로 이동

N, M = map(int, input().split())
result = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    x, y, w = map(int, input().split())
    result[x][y] = w

for i in range(1,N+1) :
    for j in range(1,N+1) :
        print(result[i][j], end=' ')
    print()