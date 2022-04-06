import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
ints = list(map(int, input().split()))

def reverse(x) :
    return int(str(x)[::-1])

def isPrime(x) :
    if x==1 :
        return False
    for i in range(2,x//2+1) : # x의 약수는 x/2 이내에만 존재함
        if x%i == 0 :
            return False
    # for ~ else 구문 기억해!!
    else :
        return True

for i in ints :
    ri = reverse(i)
    if isPrime(ri) :
        print(ri, end=' ')