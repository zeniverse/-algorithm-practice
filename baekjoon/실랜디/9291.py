t = int(input())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for test_i in range(t):
    flag = True

    if test_i > 0:
        empty = input()

    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행 검사
    for i in range(9):
        if sorted(arr[i]) != num:
            flag = False
            break

    # 열 검사
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(arr[j][i])
        if sorted(tmp) != num:
            flag = False
            break

    # 3x3 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []

            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    tmp.append(arr[k][l])

            if sorted(tmp) != num:
                flag = False
                break

    if flag:
        print('Case {}: CORRECT'.format(test_i + 1))
    else:
        print('Case {}: INCORRECT'.format(test_i + 1))

