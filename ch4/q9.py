import sys
from collections import Counter

sys.stdin = open('input.txt', 'r')

word1 = input()
word2 = input()

cnt = Counter(word1)

for w in word2:
    if w not in cnt.keys():
        break
    else:
        cnt[w] -= 1

if any(x != 0 for x in cnt.values()):
    print('NO')
else:
    print('YES')