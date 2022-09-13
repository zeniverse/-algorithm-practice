import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

start = 0
end = n - 1

for i in arr2:
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr1[mid] == i:
            print(1, end=" ")
            break

        if arr1[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0, end=" ")

