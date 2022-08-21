import heapq

scoville = [1, 2, 3, 9, 10, 12]
k = 7

heapq.heapify(scoville)
count = 0

while scoville[0] < k:

    if len(scoville) <= 1:
        print(-1)
        break

    num1 = heapq.heappop(scoville)
    num2 = heapq.heappop(scoville)

    newNum = num1 + (num2 * 2)
    heapq.heappush(scoville, newNum)
    count += 1

print(count)





