import sys

sys.stdin = open('input.txt', 'r')

# level, start(가지를 뻗는 첫번째 숫자), SUM(조합의 합)
def DFS(L, S, SUM):
    global cnt
    # L==K : 하나의 조합이 완성됨
    if L == K:
        if SUM % M == 0 :
            cnt += 1
    else:
        for i in range(S, N):
            DFS(L+1, i+1, SUM+ints[i])

if __name__ == '__main__':
    N, K = map(int, input().split())
    ints = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
