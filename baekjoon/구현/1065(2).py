import sys
input = sys.stdin.readline

def check(num):
    if num < 100:
        return True
    else:
        arr = list(map(int, str(num)))

        if arr[0] - arr[1] == arr[1] - arr[2]:
            return True


n = int(input())
res = 0

for i in range(1, n + 1):
    if check(i):
        res += 1
print(res)
