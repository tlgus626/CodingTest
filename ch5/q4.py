import sys
sys.stdin = open('input.txt', 'r')

def DFS(v):
    # 인덱스가 0부터 시작하므로 N이 종료지점!
    if v == N:
        SUM = 0
        for i in range(N) :
            if check[i] == 1 :
                SUM += S[i]
        # early stopping : TOTAL//2보다 커지는 순간 하위 노드로 뻗을 필요 없음
        if SUM > TOTAL//2 :
            return
        if SUM == TOTAL-SUM : # TOTAL//2로 하면 오류남 주의!!
            print('YES')
            # 프로그램 종료
            sys.exit(0)
    else:
        # 왼쪽 부분집합에 포함
        check[v] = 1
        DFS(v + 1)
        # 오른쪽 부분집합에 포함
        check[v] = 0
        DFS(v + 1)

if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    check = [0]*N
    TOTAL = sum(S)
    DFS(0)
    # SUM != TOTAL-SUM : 재귀함수 다 돌고(프로그램이 종료되지 않아) main으로 돌아옴
    print('NO')