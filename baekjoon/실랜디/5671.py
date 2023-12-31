import sys
input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    res = 0
    for num in range(n, m + 1):
        cnt = set()
        s_num = str(num)

        for char in s_num:
            cnt.add(char)

        if len(s_num) == len(cnt):
            res += 1
    print(res)