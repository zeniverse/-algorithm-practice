import sys, heapq
input = sys.stdin.readline

def solution(arr):
    left = []
    right = []
    mid = arr[0]
    res = [mid]

    for idx, v in enumerate(arr[1:], 1):
        if v > mid:
            heapq.heappush(right, v)
        else:
            heapq.heappush(left, -v)

        if idx % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -(heapq.heappop(left))
            elif len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            res.append(mid)

    print(len(res))

    for i in range(len(res)):
        if i != 0 and (i + 1) % 10 == 1:
            print()
        print(res[i] ,end = " ")
    print()


for _ in range(int(input().strip())):
    m = int(input().strip())
    arr = []

    for _ in range(m//10 + 1):
        arr.extend(list(map(int, input().split(' '))))

    solution(arr)