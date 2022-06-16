import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

# dynamic table : i번째 문제까지 푼다고 할 때, j분 안에 얻을 수 있는 최대 점수
# dynamic programming을 뒤에서부터 하면 중복이 발생하지 않음
dy = [0]*(M+1)

# dynamic programming
for i in range(N) :
    s, t = map(int, input().split())
    for j in range(M, t-1, -1) :
        dy[j] = max(dy[j], dy[j-t]+s)

print(dy)