import sys
sys.stdin = open('input.txt', 'rt')

N, K = map(int, input().split())
cards = list(map(int, input().split()))

unique = set()
for i in range(N) :
    for j in range(i+1,N) :
        for l in range(j+1,N) :
            unique.add(cards[i]+cards[j]+cards[l]) # set 자료구조는 append가 아니라 add

unique = list(unique)
unique.sort(reverse=True)
print(unique[K-1])