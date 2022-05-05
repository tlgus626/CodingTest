import sys
from collections import deque
sys.stdin = open('input.txt','r')

must = input()
N = int(input())

for i in range(N) :
    lecture = input()
    deq = deque(must) # 이렇게 해도 각 알파벳씩 나눠서 deque 안에 들어감
    for l in lecture :
        # 필수과목
        if l in deq :
            # 순서불일치 : 수업설계에 필수과목 순서가 다름
            if l != deq.popleft() :
                print('#%d NO' %(i+1))
                break
    else :
        # 순서일치 : 이외 조건 모두 만족
        if len(deq) == 0 :
            print('#%d YES' %(i+1))
        # 남은 필수과목 존재 : 수업설계에 필수과목이 다 안들어가있음
        else :
            print('#%d NO' % (i + 1))