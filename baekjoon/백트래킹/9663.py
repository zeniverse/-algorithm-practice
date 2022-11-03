n = int(input())

row = [0] * n
res = 0

def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i] - row[x]) == x - i:
            return False
    return True


def func(k):
    global res
    if k == n:
        res += 1
        return

    for i in range(n):
        row[k] = i
        if check(k):
            func(k + 1)

func(0)
print(res)