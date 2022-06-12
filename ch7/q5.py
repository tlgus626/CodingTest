# n번째 수를 수열의 마지막 항으로 할 때, 여러 경우의 수 중 '최대 길이'를 dy[n]으로 정의

import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dy = [0] * (N + 1)

# initialize
dy[1] = 1
# result
MAX = 0

for i in range(2, N + 1):
    m = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and dy[j] > m:
            m = dy[j]
    dy[i] = m + 1
    if dy[i] > MAX:
        MAX = dy[i]

print(MAX)
