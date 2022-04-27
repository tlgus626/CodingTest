import sys
sys.stdin = open('input.txt','r')

N = int(input())
A = list(map(int, input().split()))

lt = 0
rt = N-1
last = 0
LR = ''
seq = []

while lt <= rt :
    if A[lt] > last :
        seq.append((A[lt], 'L'))
    if A[rt] > last :
        seq.append((A[rt], 'R'))
    seq.sort() # lt or rt 중 더 작은 걸 seq에 넣어야 함
    if len(seq) == 0 :
        break
    else : # seq에 한개 또는 두개의 값이 들어가 있음
        LR += seq[0][1] # 더 작은 것의 알파벳을 더해줌
        last = seq[0][0]
        if seq[0][1] == 'L' :
            lt += 1
        else :
            rt -= 1
    seq.clear()

print(len(LR), LR, sep='\n')