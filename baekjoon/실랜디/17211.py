n, now = map(int, input().split())
g_g, g_b, b_g, b_b = map(float, input().split())

bad = 0.0
good = 0.0

if now == 0:
    good = 1.0
else:
    bad = 1.0

for _ in range(n):
    prev_good = good
    prev_bad = bad

    good = prev_good * g_g + prev_bad * b_g
    bad = prev_good * g_b + prev_bad * b_b

print(int(good * 1000))
print(int(bad * 1000))


