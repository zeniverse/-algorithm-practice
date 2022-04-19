
x, y, w, h = map(int, input().split())
a, b = x, y
a2, b2 = (w-x), (h-y)

print(min(a, b, a2, b2))