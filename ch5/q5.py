import sys
sys.stdin = open('input.txt', 'r')

def DFS(v):
    # 인덱스가 0부터 시작하므로 N이 종료지점!
    if v == N:
        SUM = 0
        global MAX
        for i in range(N) :
            if check[i] == 1 :
                SUM += dogs[i]
        if SUM > C : # cut edge
            return
        if SUM > MAX : # MAX는 지역변수인데, 함수 내에서 참조하고 있음 (update되는 값이라서)
            MAX = SUM
    else:
        # 바둑이 태움
        check[v] = 1
        DFS(v + 1)
        # 바둑이 안태움
        check[v] = 0
        DFS(v + 1)

if __name__ == '__main__':
    C, N = map(int, input().split())
    dogs = []
    for _ in range(N) :
        dogs.append(int(input()))
    check = [0]*N
    MAX = 0
    DFS(0)
    print(MAX)