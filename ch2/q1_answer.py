import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

for i in range(N) :
    word = input().lower()
    size = len(word)
    for j in range(size//2) :
        if word[j] != word[-1-j] :
            print('#%d NO' %(i+1))
            break
    # for ~ else!!!
    else :
        print('#%d YES' %(i+1))