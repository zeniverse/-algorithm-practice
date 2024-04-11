import heapq

n, m = map(int, input().split())
present = []

for i in list(map(int, input().split())):
    heapq.heappush(present, -i)

wish = list(map(int, input().split()))

flag = False

for i in wish:
    x = -heapq.heappop(present)
    if x - i < 0:
        flag = True
        break
    heapq.heappush(present, -(x - i))

if flag:
    print(0)
else:
    print(1)


