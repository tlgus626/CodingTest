import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

note = {}
for i in range(N):
    word = input()
    note[word] = 0

for i in range(N - 1):
    word = input()
    note[word] = 1

for key, value in note.items():
    if value == 0:
        print(key)
        break
