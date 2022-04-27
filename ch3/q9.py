import sys
sys.stdin = open('input.txt','r')

N = int(input())
A = list(map(int, input().split()))

last = 0
LR = ''

while True :
    if A[0] < last and A[-1] < last :
        break
    elif A[0] > last and A[-1] > last :
        if A[0] < A[-1] :
            last = A[0]
            A.pop(0)
            LR += 'L'
        else :
            last = A[-1]
            A.pop()
            LR += 'R'
    elif A[0] > last and A[-1] < last :
        last = A[0]
        A.pop(0)
        LR += 'L'
    elif A[-1] > last and A[0] < last :
        last = A[-1]
        A.pop()
        LR += 'R'

print(len(LR), LR, sep='\n')