import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

prizes = list()

for i in range(N) :
    nums = list(map(int, input().split()))
    dice = [0] * 6
    for n in nums :
        for j in range(1,7) :
            if j==n : dice[j-1] += 1
    if max(dice)==3 :
        freq = dice.index(max(dice)) + 1
        prizes.append(10000 + freq*1000)
    elif max(dice)==2 :
        freq = dice.index(max(dice)) + 1
        prizes.append(1000 + freq*100)
    else :
        d_max = max(nums)
        prizes.append(d_max*100)

print(max(prizes))