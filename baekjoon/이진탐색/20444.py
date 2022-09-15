import sys
input = sys.stdin.readline

n, k = map(int, input().split())

start = 0
end = n // 2

while start <= end:
    mid = (start + end) // 2
    colcut = n - mid 

    pieces = (mid + 1) * (colcut + 1)

    if pieces == k:
        print("YES")
        sys.exit(0)
    
    if k > pieces:
        start = mid + 1
    else:
        end = mid - 1

print("NO")