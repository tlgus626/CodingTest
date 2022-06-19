N, K = 10, 3
cards = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]

unique = set()
for i in range(N):
    for j in range(i + 1, N):
        for l in range(j + 1, N):
            unique.add(cards[i] + cards[j] + cards[l])

unique = list(unique)
unique.sort(reverse=True)
print(unique[K - 1])
