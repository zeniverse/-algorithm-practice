import heapq
import sys
input = sys.stdin.readline

n = int(input())
# leftHeap은 최대힙으로 중간값 + 중간값보다 작은 값을 넣어준다
# rightHeap은 최소힙으로 중간값 보다 큰 값을 넣어준다
leftHeap = []
rightHeap = []

for _ in range(n):
    num = int(input())

    # 순서대로 leftHeap, rightHeap 하나씩 값을 넣어준다
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    # 만약 rightHeap의 최소값 보다 leftHeap의 최대값이 크다면
    # 중간값 보다 큰 값이 leftHeap에 있다는 뜻이므로
    # 두 값의 위치를 바꿔준다.
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftNum = heapq.heappop(leftHeap)
        rightNum = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightHeap)
        heapq.heappush(rightHeap, -leftNum)

    print(-leftHeap[0])