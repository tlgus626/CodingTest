import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
coins = list(map(int, input().split()))
M = int(input())

# dynamic table
# dy[j] = j원을 만들 수 있는 최소 가짓수
dy = [500]*(M+1)

# initialize
dy[0] = 0

for c in coins :
    for j in range(c, M+1) :
        # e.g., dy[8-5]+1 = 8원을 만들기 위해, 3원을 만드는 최소 가짓수에 5원짜리 동전 하나 더하기
        dy[j] = min(dy[j], dy[j-c]+1)

print(dy)