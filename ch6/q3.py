import sys

sys.stdin = open('input.txt', 'r')

def DFS(L, C):
    if C == N:
        if L > 0 and L <= sum(W) :
            S[L] = 1
    else:
        for i in range(N) :
            if check[i] == 0:
                # 저울의 왼쪽에 추를 둠
                check[i] = 1
                DFS(L-W[i], C+1)
                check[i] = 0
                # 저울의 오른쪽에 추를 둠
                check[i] = 1
                DFS(L+W[i], C+1)
                check[i] = 0
                # 저울에 추를 두지 않음
                DFS(L, C+1)

if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    S = [0]*sum(W)
    S.insert(0, 1)
    check = [0]*N
    DFS(0, 0)
    cnt = 0
    for s in S :
        if s == 0 :
            cnt += 1
    print(cnt)