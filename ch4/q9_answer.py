import sys

sys.stdin = open('input.txt', 'r')

word1 = input()
word2 = input()

str1 = dict()
str2 = dict()

for w in word1 :
    # get() : w가 없으면 0, 있으면 value값 리턴
    str1[w] = str1.get(w, 0) + 1

for w in word2 :
    str2[w] = str2.get(w, 0) + 1

# dictionary 같은지?
for i in str1.keys() :
    if i in str2.keys() :
        if str1[i] != str2[i] :
            print('NO')
            break
    else :
        print('NO')
        break
else :
    print('YES')