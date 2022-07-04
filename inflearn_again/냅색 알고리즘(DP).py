N, L = 4, 11
WV = [(5, 12), (3, 8), (6, 14), (4, 8)]

dy = [0] * (L + 1)

for w, v in WV:
    for i in range(w, L + 1):
        dy[i] = max(dy[i], dy[i - w] + v)

print(dy)
