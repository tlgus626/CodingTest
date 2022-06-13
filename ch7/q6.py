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
