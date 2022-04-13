import sys
sys.stdin = open('input2.txt','rt')

N = int(input())
# 여러 줄을 반복문으로 불러와서 2차원 list 생성
nums = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
sums = list()

diag_sum1 = 0
diag_sum2 = 0

for i in range(N) :
    row_sum = 0
    col_sum = 0
    for j in range(N) :
        row_sum += nums[i][j]
        col_sum += nums[j][i]

    diag_sum1 += nums[i][i]
    diag_sum2 += nums[i][N-1-i]

    if row_sum > max_sum : max_sum = row_sum
    if col_sum > max_sum : max_sum = col_sum
    if diag_sum1 > max_sum : max_sum = diag_sum1
    if diag_sum2 > max_sum : max_sum = diag_sum2

print(max_sum)