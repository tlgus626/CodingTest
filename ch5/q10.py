import sys

sys.stdin = open('input.txt', 'r')

# level, start(가지를 뻗는 첫번째 숫자)
def DFS(L, S):
    global cnt
    # L==M : 하나의 조합이 완성됨
    if L == M:
        for j in range(M):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(S, N + 1):
            result[L] = i
            DFS(L+1, i+1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    result = [0] * (N+1)  # 최종 조합
    cnt = 0
    DFS(0, 1)
    print(cnt)
