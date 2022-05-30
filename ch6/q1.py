import sys

sys.stdin = open('input.txt', 'r')


# level, score, time
def DFS(L, S, T):
    global MAX
    # time out
    if T > M :
        return
    # 모든 문제 검토해서 확인함
    if L == N:
        if S > MAX:
            MAX = S
    else:
        # 이 문제 풀고 지나감
        DFS(L+1, S+ST[L][0], T+ST[L][1])
        # 이 문제 안풀고 지나감
        DFS(L+1, S, T)

if __name__ == '__main__':
    N, M = map(int, input().split())
    ST = []
    for _ in range(N):
        s, t = map(int, input().split())
        ST.append((s, t))
    MAX = 0
    DFS(0, 0, 0)
    print(MAX)