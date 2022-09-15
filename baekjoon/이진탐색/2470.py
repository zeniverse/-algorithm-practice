
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1

diff = abs(arr[left] + arr[right])
res = [arr[left], arr[right]]

while left < right:
    value_left = arr[left]
    value_right = arr[right]

    total = value_left + value_right

    if diff > abs(total):
        diff = abs(total)
        res = [arr[left], arr[right]]

    if total < 0:
        left += 1
    else:
        right -= 1

print(res[0], res[1])
