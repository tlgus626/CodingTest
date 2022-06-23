N = '9977252641'
M = 5

stack = []

for n in N:
    while stack and M > 0 and stack[-1] < n:
        stack.pop()
        M -= 1
    stack.append(n)

if M != 0:
    stack = stack[:-M]

for s in stack:
    print(s, end='')