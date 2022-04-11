import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

for i in range(N) :
    word = input().lower()
    word_r = word[::-1]
    if word == word_r :
        print('#%d YES' %(i+1))
    else :
        print('#%d NO' %(i+1))