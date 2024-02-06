
n, m = map(int, input().split())
j = int(input())

start = 1
end = m
count = 0

for _ in range(j):
    apple = int(input())

    if start <= apple and end >= apple:
        continue
    elif apple > start:
        count += (apple - end)
        start += (apple - end)
        end = apple
    else:
        count += (start - apple)
        end -= (start - apple)
        start = apple

print(count)
        