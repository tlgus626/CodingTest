import sys

sys.stdin = open('input.txt', 'r')

# level : k번째 동전을 0~p[k]개 중에 몇 개 쓸지?
def DFS(L, S):
    global cnt
    # cut
    if S > T :
        return
    # K개 동전 경우의 수 고려 다 함
    if L == K :
        if S == T :
            cnt += 1
    else :
        # L번째 동전을 0개 사용 ~ MAX개 사용
        for i in range(PN[L][1]+1) :
            # e.g., i=1이면 L번째 동전 1개 사용
            DFS(L+1, S+PN[L][0]*i)

if __name__ == '__main__':
    T = int(input())
    K = int(input())
    PN = list()
    for _ in range(K) :
        p, n = map(int, input().split())
        PN.append((p,n))
    cnt = 0
    DFS(0, 0)
    print(cnt)