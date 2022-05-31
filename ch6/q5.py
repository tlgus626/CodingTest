import sys

sys.stdin = open('input.txt', 'r')


def DFS(L):
    global DIFF
    if L == N:
        if max(ABC) - min(ABC) < DIFF :
            # 중복 값이 있는지 확인
            tmp = set()
            for i in ABC :
                tmp.add(i)
            if len(tmp) == 3:
                DIFF = max(ABC) - min(ABC)
    else:
        # 3명 중 누구에게 L번째 동전을 나눠줄 것인가?
        for i in range(3) :
            ABC[i] += coins[L]
            DFS(L+1)
            ABC[i] -= coins[L]

if __name__ == '__main__':
    N = int(input())
    coins = list()
    for _ in range(N):
        coins.append(int(input()))
    ABC = [0]*3
    DIFF = float('inf')
    DFS(0)
    print(DIFF)
