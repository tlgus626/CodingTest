import sys

sys.stdin = open('input.txt', 'r')

def DFS(L, SUM) :
    if L == N and SUM == F :
        for p in P :
            print(p, end=' ')
        # 사전 순으로 가장 앞에 오는 것만 출력하고 프로그램 종료
        sys.exit(0)
    else:
        for i in range(1, N + 1):
            # i를 사용하지 않았을 경우에만 재귀
            if check[i] == 0:
                check[i] = 1  # i를 이미 사용했음을 체크
                P[L] = i  # 순열에 i를 담음
                DFS(L + 1, SUM+P[L]*B[L])
                check[i] = 0  # i를 사용한 사실을 다시 해제

if __name__ == '__main__':
    N, F = map(int, input().split())
    P = [0] * N # permutation
    B = [1] * N # 이항정리 계수
    # B의 첫항과 마지막항은 계수가 항상 1이므로 두번째부터 for문 돌면 됨
    for i in range(1,N-1) :
        B[i] = (B[i-1] * (N-i))/i
    check = [0] * (N+1) # 순열에서 중복을 방지하기 위한 체크리스트
    DFS(0, 0)