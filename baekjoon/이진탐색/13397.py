
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 구간을 나눠 count 하는 함수
def divided(x):
    max_ = min_ = arr[0]
    count = 1

    for i in range(1, n):
        max_ = max(max_, arr[i])
        min_ = min(min_, arr[i])

        diff = max_ - min_

        if diff > x:
            count += 1
            max_ = arr[i]
            min_ = arr[i]

    return count


start = 0
end = max(arr)
res = 0

while start <= end:
    # mid는 각 구간별 (최대값 - 최소값) 의 최대값 중 최소값
    mid = (start + end) // 2

    if divided(mid) <= m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)