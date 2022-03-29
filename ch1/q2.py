import sys
sys.stdin = open('input.txt', 'rt')

T = int(input()) # case 개수 = 제일 첫 번째 줄 2

for t in range(T) :
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort() # 이렇게 해도 sort가 반영 되나봐
    print('#%d %d' %(t+1, a[k-1])) # 이 방법 기억하자!!