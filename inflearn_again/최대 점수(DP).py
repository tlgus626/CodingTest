N, M = 5, 20
ST = [(10, 5), (25, 12), (15, 8), (6, 3), (7, 4)]

dy = [0] * (M + 1)

for s, t in ST:
    # the number of question is one -> start dynamic programming from 'last'
    for i in range(M, t - 1, -1):
        dy[i] = max(dy[i], dy[i - t] + s)

print(dy)
