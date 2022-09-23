import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

if max(arr) == 0:
    print('SAD')
else:
    value = sum(arr[:x])

    max_ = value
    count = 1

    for i in range(x, n):
        value += arr[i]
        value -= arr[i - x]

        if value > max_:
            max_ = value
            count = 1
        
        elif value == max_:
            count += 1

    print(max_)
    print(count)