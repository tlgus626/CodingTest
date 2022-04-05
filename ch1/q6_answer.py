import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
nums = list(map(int, input().split()))

def digit_sum(x) :
    sum = 0
    # 자릿수합 기억하자..
    while x>0 :
        sum += x%10 # 나머지
        x = x//10 # 몫
    return sum

max_sum = 0

for i in range(N) :
    d = digit_sum(nums[i])
    if d > max_sum :
        max_sum = d
        max_id = nums[i] # 굳이 max_id 미리 지정할 필요 없음!!

print(max_id)