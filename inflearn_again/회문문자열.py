N = 5
words = ['level', 'moon', 'abcba', 'soon', 'gooG']

for i in range(N):
    word = words[i]
    size = len(word)
    for j in range(size // 2):
        if word[j] != word[-1 - j]:
            print('#%d NO' % (i + 1))
            break
    else:
        print('#%d YES' % (i + 1))
