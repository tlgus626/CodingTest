import sys

sys.stdin = open('input.txt', 'r')


def DFS(v):
    global cnt
    # v==M : 하나의 중복순열이 완성됨
    if v == M:
        for j in range(M):
            print(result[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N + 1):
            # i를 사용하지 않았을 경우에만 재귀
            if check[i] == 0:
                check[i] = 1  # i를 이미 사용했음을 체크
                result[v] = i  # 순열에 i를 담음
                DFS(v + 1)
                check[i] = 0  # i를 사용한 사실을 다시 해제


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = [0] * (N + 1)  # i를 사용했는지 확인하기 위한 체크리스트
    result = [0] * M  # 최종 순열
    cnt = 0
    DFS(0)
    print(cnt)
