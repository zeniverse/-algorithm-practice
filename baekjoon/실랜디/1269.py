a_count, b_count = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

print(len(a - b) + len(b - a))