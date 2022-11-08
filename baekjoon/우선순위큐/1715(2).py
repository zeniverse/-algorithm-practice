import heapq
import sys
input = sys.stdin.readline

n = int(input())
card = []
res = 0

for _ in range(n):
    heapq.heappush(card, int(input()))

# while card: 로 while문을 돌리게 되면 에러가남
# 두개씩 뽑아내야 하기 때문에 길이가 1보다 클때 까지 while문이 돌아가도록 해야한다
#  ex) 10, 20, 40 일때 계산을 다 하고, 마지막에 100이 card에 남아있기 때문이다.
while len(card) > 1:
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)

    res += n1 + n2

    heapq.heappush(card, n1 + n2)

print(res)

