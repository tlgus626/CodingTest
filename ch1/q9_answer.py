import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

max_prize = 0

for i in range(N) :
    nums = input().split() # int로 맵핑 안되고, string
    nums.sort()
    a, b, c = map(int, nums) # a:smallest, c:largest
    if a==b and b==c :
        prize = 10000 + c*1000
    elif a==b or a==c :
        prize = 1000 + a*100
    elif b==c :
        prize = 1000 + b*100
    else :
        prize = c*100
    if prize > max_prize :
        max_prize = prize

print(max_prize)