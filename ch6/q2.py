import sys

sys.stdin = open('input.txt', 'r')

# level, profit
def DFS(L, P):
    global result
    # N+1일 째에 휴가를 떠나므로 소요시간을 더했을 때, N+1을 넘으면 안됨
    if L > N+1 :
        return
    if L == N+1 :
        if P > result :
            result = P
    else:
        # 상담 진행
        DFS(L+TP[L][0], P+TP[L][1])
        # 상담 미진행
        DFS(L+1, P)
    # else : if L+TP[L][0] <= N+1 : DFS(L+TP[L][0], P+TP[L][1]) 이렇게 전개하는 방식도 있음!

if __name__ == '__main__':
    N = int(input())
    TP = list()
    for _ in range(N) :
        t, p = map(int, input().split())
        TP.append((t,p))
    result = 0
    # 1일부터 상담 시작!
    TP.insert(0, (0,0))
    DFS(1, 0)
    print(result)