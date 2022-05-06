import sys
sys.stdin = open('input.txt','r')

N = int(input())

note = {}
for _ in range(2*N-1) :
    k = input()
    if k not in note.keys() :
        note[k] = 0
    else :
        note[k] = 1

for k, v in note.items() :
    if v == 0 :
        print(k)