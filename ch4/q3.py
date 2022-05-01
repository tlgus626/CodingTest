import sys
sys.stdin = open('input.txt','r')

eq = [i for i in input()]

res = ''
stack = []

while eq :
    if eq[0].isdigit() :
        res += eq[0]
    else :
        stack.append(eq[0])
    eq.pop(0)
else :
    while stack :
        res += stack[-1]
        stack.pop()

print(res)

# 결국 괄호 문제를 해결하지 못함 ㅠㅠ