import sys
sys.stdin = open('input2.txt','rt')

A = [list(map(int, input().split())) for _ in range(9)]

def check(A) :
    # row, column count
    for i in range(9) :
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9) :
            ch1[A[i][j]] = 1
            ch2[A[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9 :
            print('NO')
    # box count
    for i in range(3) :
        for j in range(3) :
            ch3 = [0]*10
            for k in range(3) :
                for s in range(3) :
                    ch3[A[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9 :
                print('NO')
    else :
        print('YES')

check(A)