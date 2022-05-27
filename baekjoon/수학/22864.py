import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())
work = 0
tired = 0
time = 0

if a > m:
    print(0)
else:
    while time != 24:
        time += 1

        if tired + a <= m:
            work += b
            tired += a
        else:
            if tired - c >= 0:
                tired -= c
            else:
                tired = 0

    print(work)
