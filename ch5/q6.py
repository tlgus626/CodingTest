import sys
sys.stdin = open('input.txt', 'r')

# 이진상태트리가 아니라 n가닥으로 뻗는 상태트리! : for문이 돌면서 n개 노드로 확장
# DFS(v) : 순열 내 원소 개수가 v개 (v==m개까지 재귀)

def DFS(v):
    global cnt
    # v==M : 하나의 중복순열이 완성됨
    if v == M :
        for i in range(M) :
            print(check[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1) :
            check[v] = i # check = [i, i] 이런 식으로 순열을 완성함
            DFS(v+1) # 원소 개수가 v+1개인 순열을 만들기 위해 재귀
        # check[v]=1, DFS(v+1) ; check[v]=2, DFS(v+1) ; check[v]=3, DFS(v+1) 실행하는 것

if __name__ == '__main__':
    N, M = map(int, input().split())
    check = [0]*M
    cnt = 0
    DFS(0)
    print(cnt)