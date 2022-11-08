import heapq
import sys
input = sys.stdin.readline

def solution(n, card):

    if n == 1:
        return 0

    for _ in range(n):
        heapq.heappush(card, int(input()))

    res = 0

    #heapq에서 두개씩 뽑아내야 하므로 n-1까지 for문을 돌려준다
    for i in range(n - 1):
        prev = heapq.heappop(card)
        cur = heapq.heappop(card)

        res += (prev + cur)

        heapq.heappush(card, prev + cur)

    return res

n = int(input())
card = []

print(solution(n, card))
