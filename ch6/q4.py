import sys

sys.stdin = open('input.txt', 'r')

def DFS(S):
    if S > T :
        return
    if S == T :
        res.add(tuple(check))
    else :
        for i in range(K) :
            if check[i] < PN[i][1] :
                check[i] += 1
                DFS(S+PN[i][0])
                check[i] -= 1

if __name__ == '__main__':
    T = int(input())
    K = int(input())
    PN = list()
    for _ in range(K) :
        p, n = map(int, input().split())
        PN.append((p,n))
    check = [0]*K
    res = set()
    DFS(0)
    print(len(res))