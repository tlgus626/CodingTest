N = 3
a = [1, 3, 5]
M = 5
b = [2, 3, 6, 7, 9]

p1 = p2 = 0
c = list()

while p1 < N and p2 < M:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < N:
    c = c + a[p1:]
if p2 < M:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')
