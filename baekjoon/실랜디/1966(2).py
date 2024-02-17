from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque([(i, arr[i]) for i in range(n)])

    arr.sort()
    count = 0

    while queue:
        idx, rank = queue.popleft()

        if rank == arr[-1]:
            arr.pop()
            count += 1

            if idx == m:
                print(count)
                break

        else:
            queue.append((idx, rank))

