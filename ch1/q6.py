import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
nums = list(map(int, input().split()))

def digit_sum(x) :
    d = [int(i) for i in str(x)]
    return sum(d)

max_sum = 0

for i in range(N) :
    d = digit_sum(nums[i])
    if d > max_sum :
        max_sum = d
        max_id = nums[i]

print(max_id)