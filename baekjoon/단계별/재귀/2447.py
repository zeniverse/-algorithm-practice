import sys
sys.setrecursionlimit(10**6)


def append_start(LEN):

    if LEN == 1:
        return ['*']

    stars = append_start(LEN//3)
    arr = []

    for s in stars:
        arr.append(s * 3)

    for s in stars:
        arr.append(s + ' '*(LEN//3) + s)

    for s in stars:
        arr.append(s*3)

    return arr



n = int(sys.stdin.readline().strip())
print('\n'.join(append_start(n)))

