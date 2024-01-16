n, m = map(int, input().split())
package, single = [], []
res = 0

for _ in range(m):
    p, s = map(int, input().split())
    package.append(p)
    single.append(s)

min_p = min(package)
min_s = min(single)

if min_p < min_s * 6:
    if min_p < (n % 6) * min_s:
        print((n // 6) * min_p + min_p)
    else:
        print((n // 6) * min_p + (n % 6) * min_s)

elif min_p >= min_s * 6:
    print(min_s * n)