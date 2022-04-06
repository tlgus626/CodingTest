import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
ints = list(map(int, input().split()))

def reverse(x) :
    return int(str(x)[::-1])

def isPrime(x) :
    mod = []
    for i in range(1,x+1) :
        if x%i==0 : mod.append(i)
    if mod == [1,x] :
        return True
    else :
        return False

rev_prime = []

for i in ints :
    ri = reverse(i)
    if isPrime(ri) == True :
        rev_prime.append(ri)

print(rev_prime)