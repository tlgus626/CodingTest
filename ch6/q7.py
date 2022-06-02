import sys

sys.stdin = open('input.txt', 'r')


# LEVEL, COUNT
def BFS(L, C):
    global MIN
    if C > MIN:
        return
    if L == E:
        if C < MIN:
            MIN = C
    else:
        BFS(L + 1, C + 1)
        BFS(L - 1, C + 1)
        BFS(L + 5, C + 1)


if __name__ == '__main__':
    S, E = map(int, input().split())
    MIN = float('inf')
    BFS(S, 0)
    print(MIN)
