import sys

sys.stdin = open('input.txt', 'r')

def DFS(L, C):
    global res
    if C == N:
        if L > 0 and L <= S :
            res.add(L)
    else:
        # 저울의 왼쪽에 추를 둠
        DFS(L - W[C], C + 1)
        # 저울의 오른쪽에 추를 둠
        DFS(L + W[C], C + 1)
        # 저울에 추를 두지 않음
        DFS(L, C + 1)

if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    res = set() # 측정 가능한 무게 카운트
    DFS(0, 0)
    print(S-len(res))