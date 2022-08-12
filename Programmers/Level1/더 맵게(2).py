import heapq

# 1번 풀이 방법보다 효율성 확인하는 속도가 더 빠름

def solution(scoville, K):

    heapq.heapify(scoville)
    count = 0

    while True:
        num1 = heapq.heappop(scoville)

        if num1 >= K:
            break
        
        if len(scoville) == 0:
            return -1

        num2 = heapq.heappop(scoville)

        heapq.heappush(scoville, num1 + (num2 * 2))
        count += 1

    return count







