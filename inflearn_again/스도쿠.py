A = [[1, 4, 3, 6, 2, 8, 5, 7, 9],
     [5, 7, 2, 1, 3, 9, 4, 6, 8],
     [9, 8, 6, 7, 5, 4, 2, 3, 1],
     [3, 9, 1, 5, 4, 2, 7, 8, 6],
     [4, 6, 8, 9, 1, 7, 3, 5, 2],
     [7, 2, 5, 8, 6, 3, 9, 1, 4],
     [2, 3, 7, 4, 8, 1, 6, 9, 5],
     [6, 1, 9, 2, 7, 5, 8, 4, 3],
     [8, 5, 4, 3, 9, 6, 1, 2, 7]]


def check(A):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[A[i][j]] = 1
            ch2[A[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            print('NO')
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[A[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                print('NO')
    else:
        print('YES')


check(A)
