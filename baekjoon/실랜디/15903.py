from sys import stdin
import heapq


n, m = map(int, stdin.readline().split())

cards = [int(x) for x in stdin.readline().split()]
# cards 리스트를 heap으로 변환
heapq.heapify(cards)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))