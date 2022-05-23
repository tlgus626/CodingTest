import sys

sys.stdin = open('input.txt', 'r')

def DFS(L):
    global cnt
    if L == N :
        cnt += 1
        print(path)
    else :
        for i in range(1, N+1) :
            # 노드 i로 연결 가능
            if graph[L][i] == 1 and check[i] == 0 :
                check[i] = 1
                # 노드 i로 연결!
                path.append(i)
                # 노드 i로 연결!
                DFS(i)
                # back
                path.pop()
                check[i] = 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
    cnt = 0
    path = []
    # 1번 노드 방문한 뒤에 DFS 시작
    path.append(1)
    check = [0]*(N+1)
    # 1번 노드 방문한 뒤에 DFS 시작해야지!!
    check[1] = 1
    DFS(1)
    print(cnt)