s, c = map(int, input().split())
arr = []

for _ in range(s):
    arr.append(int(input()))

start = 1
end = max(arr)

rest = 0

while start <= end:
    mid = (start + end) // 2

    count = sum(i // mid for i in arr)

    if count >= c:
        rest = max(rest, mid)
        start = mid + 1

    else:
        end = mid - 1

print(sum(arr) - (rest * c))