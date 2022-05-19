import sys

sys.stdin = open('input.txt', 'r')

# level, start(가지를 뻗는 첫번째 숫자)
def DFS(L, S):
    global cnt
    # L==K : 하나의 조합이 완성됨
    if L == K:
        SUM = 0
        for j in range(K) :
            SUM += ints[result[j]-1]
        if SUM % M == 0 :
            cnt += 1
    else:
        for i in range(S, N + 1):
            result[L] = i
            DFS(L+1, i+1)


if __name__ == '__main__':
    N, K = map(int, input().split())
    ints = list(map(int, input().split()))
    M = int(input())
    result = [0] * (K+1)  # 최종 조합
    cnt = 0
    DFS(0, 1)
    print(cnt)
