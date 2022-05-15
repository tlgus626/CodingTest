import sys

sys.stdin = open('input.txt', 'r')


def DFS(L, SUM):
    global cnt
    if L >= cnt : # cut edge : 동전의 개수가 cnt(현재 최솟값)보다 커지면 바로 재귀 종료
        return
    if SUM > M:
        return
    if SUM == M:
        if L < cnt:
            cnt = L
    else:
        for i in range(N):
            # 동전의 개수(level)는 하나씩 증가
            # 동전 금액은 coins[i]원씩 증가
            DFS(L + 1, SUM + coins[i])


if __name__ == '__main__':
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    cnt = M + 1
    coins.sort(reverse=True)  # 내림차순으로 정렬해서 큰 단위부터 계산하면 재귀가 빨리 끝남!
    DFS(0, 0)
    print(cnt)
